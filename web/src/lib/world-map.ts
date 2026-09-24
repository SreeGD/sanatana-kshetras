import { feature } from 'topojson-client';
import type { Topology, GeometryCollection } from 'topojson-specification';
import type { MultiPolygon } from 'geojson';
// world-atlas ships no types of its own.
import landTopology from 'world-atlas/land-110m.json';

export const WORLD_MAP_WIDTH = 960;
export const WORLD_MAP_HEIGHT = 480;

function project(lng: number, lat: number): [number, number] {
  const x = ((lng + 180) / 360) * WORLD_MAP_WIDTH;
  const y = ((90 - lat) / 180) * WORLD_MAP_HEIGHT;
  return [x, y];
}

export function projectPoint(lat: number, lng: number): [number, number] {
  return project(lng, lat);
}

/**
 * A viewBox string cropped to the padded bounding box of a set of points, in the same
 * projected coordinate space as projectPoint()/buildLandPath() — for zooming a map into
 * a region (e.g. India + Nepal) rather than showing the whole world.
 */
export function boundingViewBox(points: { lat: number; lng: number }[], paddingDeg = 3): string {
  const lats = points.map((p) => p.lat);
  const lngs = points.map((p) => p.lng);
  const latMin = Math.max(-90, Math.min(...lats) - paddingDeg);
  const latMax = Math.min(90, Math.max(...lats) + paddingDeg);
  const lngMin = Math.max(-180, Math.min(...lngs) - paddingDeg);
  const lngMax = Math.min(180, Math.max(...lngs) + paddingDeg);
  const [x0, y0] = projectPoint(latMax, lngMin);
  const [x1, y1] = projectPoint(latMin, lngMax);
  return `${x0.toFixed(2)} ${y0.toFixed(2)} ${(x1 - x0).toFixed(2)} ${(y1 - y0).toFixed(2)}`;
}

/** Renders the world's landmasses (Natural Earth 110m, via world-atlas) as one SVG path string. */
export function buildLandPath(): string {
  const topology = landTopology as unknown as Topology;
  const land = feature(topology, topology.objects.land as GeometryCollection);
  const geometry = land.features[0].geometry as MultiPolygon;
  const parts: string[] = [];
  for (const polygon of geometry.coordinates) {
    for (const ring of polygon) {
      const d = ring
        .map(([lng, lat], i) => {
          const [x, y] = project(lng, lat);
          return `${i === 0 ? 'M' : 'L'}${x.toFixed(2)},${y.toFixed(2)}`;
        })
        .join(' ');
      parts.push(`${d} Z`);
    }
  }
  return parts.join(' ');
}

export interface CountryBubble {
  country: string;
  count: number;
  lat: number;
  lng: number;
}

interface TempleLike {
  data: {
    country: string;
    coordinates?: { lat: number; lng: number };
  };
}

/**
 * One bubble per country: count is every temple in that country, position is the
 * average coordinates of whichever of that country's temples have them. A country
 * with temples but none carrying coordinates yet is skipped rather than guessed at.
 */
export function aggregateByCountry(temples: TempleLike[]): CountryBubble[] {
  const counts = new Map<string, number>();
  const sums = new Map<string, { lat: number; lng: number; n: number }>();

  for (const t of temples) {
    const country = t.data.country;
    counts.set(country, (counts.get(country) ?? 0) + 1);
    if (t.data.coordinates) {
      const s = sums.get(country) ?? { lat: 0, lng: 0, n: 0 };
      s.lat += t.data.coordinates.lat;
      s.lng += t.data.coordinates.lng;
      s.n += 1;
      sums.set(country, s);
    }
  }

  const bubbles: CountryBubble[] = [];
  for (const [country, count] of counts) {
    const s = sums.get(country);
    if (!s) continue;
    bubbles.push({ country, count, lat: s.lat / s.n, lng: s.lng / s.n });
  }
  return bubbles.sort((a, b) => b.count - a.count);
}
