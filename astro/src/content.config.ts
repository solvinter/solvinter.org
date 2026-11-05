import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
const projects=defineCollection({loader:glob({pattern:'**/*.md',base:'./src/content/projects'}),schema:z.object({title:z.string(),description:z.string(),status:z.enum(['Idé','Pågående','Klart'])})});
export const collections={projects};
