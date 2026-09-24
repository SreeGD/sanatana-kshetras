import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Mirrors specs/001-temples-directory/contracts/common.schema.json
const tradition = z.enum(['vaishnava', 'shaiva', 'shakta', 'smarta', 'folk_regional', 'other']);
const continent = z.enum(['asia', 'europe', 'africa', 'north-america', 'south-america', 'oceania']);

const sourceCitation = z.object({
  type: z.enum(['scripture', 'oral_tradition', 'historical_record']),
  text: z.string().optional(),
  reference: z.string().optional(),
  note: z.string().optional(),
});

const altName = z.object({
  language: z.string().optional(),
  script: z.string().optional(),
  value: z.string(),
});

// Mirrors specs/001-temples-directory/contracts/temple.schema.json
const temples = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../content/temples' }),
  schema: z.object({
    id: z.string(),
    name: z.string(),
    alt_names: z.array(altName).optional(),
    deities: z.array(z.string()).min(1),
    traditions: z.array(tradition).min(1),
    continent,
    country: z.string(),
    region: z.string().optional(),
    city: z.string(),
    coordinates: z.object({ lat: z.number(), lng: z.number() }).optional(),
    address: z.string().optional(),
    worship_status: z.enum(['active', 'heritage', 'partially_active']),
    darshan_hours: z.string().optional(),
    best_time_to_visit: z.string(),
    festivals: z.array(z.object({ name: z.string(), approx_date: z.string() })).optional(),
    how_to_reach: z.string(),
    access_notes: z.string().optional(),
    associated_saints: z.array(z.string()).optional(),
    sources: z.array(sourceCitation).min(1),
    documented_vs_legend: z.enum(['documented', 'legend', 'mixed']),
    images: z.array(z.string()).optional(),
    divya_desam_ref: z.string().optional(),
    status: z.enum(['verified', 'pending']),
    duplicate_of: z.string().optional(),
    review_flags: z.array(z.string()).min(1).optional(),
  }),
});

// Mirrors specs/001-temples-directory/contracts/divya-desam.schema.json
const divyaDesam = defineCollection({
  loader: glob({ pattern: '*.md', base: '../content/divya-desam' }),
  schema: z.object({
    seq: z.number().int().min(1).max(108),
    id: z.string(),
    name: z.string(),
    region_group: z.enum([
      'chola-nadu', 'nadu-nadu', 'thondai-nadu', 'malai-nadu', 'pandya-nadu', 'vada-nadu', 'celestial',
    ]),
    physical: z.boolean(),
    temple_ref: z.string().optional(),
    country: z.enum(['india', 'nepal']).optional(),
    celestial_note: z.string().optional(),
    locked: z.literal(true),
    review_flags: z.array(z.string()).min(1).optional(),
    sources: z.array(sourceCitation).min(1).optional(),
  }),
});

// Mirrors specs/001-temples-directory/contracts/realm.schema.json
const beyondEarth = defineCollection({
  loader: glob({ pattern: '*.md', base: '../content/beyond-earth' }),
  schema: z.object({
    id: z.string(),
    name: z.string(),
    category: z.enum(['loka', 'spiritual-world']),
    governing_deity: z.string().optional(),
    position_in_cosmology: z.string().optional(),
    review_flags: z.array(z.string()).min(1).optional(),
    tradition_accounts: z.array(
      z.object({
        tradition,
        description: z.string(),
        sources: z.array(sourceCitation).min(1),
      })
    ).min(1),
  }),
});

// Mirrors specs/001-temples-directory/contracts/deity.schema.json
const deities = defineCollection({
  loader: glob({ pattern: '*.md', base: '../content/deities' }),
  schema: z.object({
    id: z.string(),
    name: z.string(),
    traditions: z.array(tradition).min(1),
    iconography_notes: z.string().optional(),
    match_keywords: z.array(z.string().min(2)).min(1),
    sources: z.array(sourceCitation).min(1).optional(),
  }),
});

export const collections = { temples, 'divya-desam': divyaDesam, 'beyond-earth': beyondEarth, deities };
