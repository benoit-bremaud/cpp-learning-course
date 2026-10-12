import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema({ extend: z.object({
    examples: z.array(z.string()).optional(),
  }) }) }),
  examples: defineCollection({
    loader: glob({ pattern: '**/*.md', base: './src/content/examples' }),
    schema: z.object({
      id: z.string().regex(/^[a-z][a-z0-9-]*$/),
      title: z.string().min(1),
      category: z.enum(['other-contexts', 'deeper']),
      prerequisites: z.array(z.string()),
    }),
  }),
};
