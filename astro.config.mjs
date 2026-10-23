import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// The owner approved a default export exclusively for this framework configuration.
export default defineConfig({
  site: 'https://cpp.benoitbremaud.fr',
  base: '/',
  integrations: [starlight({
    title: 'C++ embarqué',
    description: 'Comprendre, concevoir en UML, puis programmer sur microcontrôleur.',
    locales: { root: { label: 'Français', lang: 'fr' } },
    components: { Footer: './src/components/CourseFooter.astro' },
    customCss: ['./src/styles/custom.css'],
    sidebar: [
      { label: 'Bienvenue', slug: '' },
      { label: 'Parcours progressif', slug: 'parcours' },
      { label: 'Du source au programme', slug: 'du-source-au-programme' },
      { label: 'Concevoir avant de coder', slug: 'methode-uml' },
      { label: 'Pratiquer dans son IDE', slug: 'pratique' },
      { label: 'Exemple guidé du voyant', slug: 'exemple-voyant' },
      { label: 'Premières notions', items: [{ slug: 'notions/tool-01' }, { slug: 'notions/programme-minimal' }, { slug: 'notions/cpp-01' }, { slug: 'notions/cpp-09' }] },
    ],
  })],
});
