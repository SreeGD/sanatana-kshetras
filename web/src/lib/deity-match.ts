// Ports scripts/validate_content.py's cmd_deity_report matching logic exactly:
// word-boundary, case-insensitive keyword matching against each temple's free-text
// `deities` field, plus a traditions-only fallback for temples that match no keyword.
// Keep this in sync with the Python implementation if that logic ever changes.

import type { CollectionEntry } from 'astro:content';

type Temple = CollectionEntry<'temples'>;
type Deity = CollectionEntry<'deities'>;

const FALLBACK_TARGET: Record<string, string> = {
  vaishnava: 'vishnu-other',
  shaiva: 'shiva',
  shakta: 'devi-shakti',
};

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function buildPattern(keywords: string[]): RegExp {
  return new RegExp('\\b(' + keywords.map(escapeRegExp).join('|') + ')\\b', 'i');
}

export interface DeityMatchResult {
  /** deity id -> temples matching it (by keyword or fallback) */
  byDeity: Map<string, Temple[]>;
  /** temple id -> deity ids it matched (for cross-links on a temple page) */
  byTemple: Map<string, string[]>;
  uncategorized: Temple[];
}

export function computeDeityMatches(temples: Temple[], deities: Deity[]): DeityMatchResult {
  const patterns = deities.map((d) => ({ id: d.data.id, pattern: buildPattern(d.data.match_keywords) }));
  const byDeity = new Map<string, Temple[]>(deities.map((d) => [d.data.id, []]));
  const byTemple = new Map<string, string[]>();
  const uncategorized: Temple[] = [];

  for (const temple of temples) {
    const deityText = temple.data.deities.join(' | ');
    const matchedIds: string[] = [];
    for (const { id, pattern } of patterns) {
      if (pattern.test(deityText)) {
        byDeity.get(id)!.push(temple);
        matchedIds.push(id);
      }
    }

    if (matchedIds.length === 0) {
      const relevant = temple.data.traditions.filter((t) => t in FALLBACK_TARGET);
      if (relevant.length === 1) {
        const targetId = FALLBACK_TARGET[relevant[0]];
        byDeity.get(targetId)?.push(temple);
        matchedIds.push(targetId);
      }
    }

    if (matchedIds.length === 0) {
      uncategorized.push(temple);
    } else {
      byTemple.set(temple.id, matchedIds);
    }
  }

  return { byDeity, byTemple, uncategorized };
}
