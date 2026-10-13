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
    customCss: ['./src/styles/custom.css'],
    components: { Footer: './src/components/CourseFooter.astro' },
    sidebar: [
      { label: 'Retour au portfolio', link: 'https://benoitbremaud.fr/' },
      { label: 'Bienvenue', slug: '' },
      { label: 'Parcours progressif', slug: 'parcours' },
      { label: 'Du source au programme', slug: 'du-source-au-programme' },
      { label: 'Concevoir avant de coder', slug: 'methode-uml' },
      { label: 'Pratiquer dans son IDE', slug: 'pratique' },
      { label: 'Exemple guidé du voyant', slug: 'exemple-voyant' },
      { label: 'Premières notions', items: [{ slug: 'notions/tool-01' }, { slug: 'notions/programme-minimal' }, { slug: 'notions/premiers-affichages' }, { slug: 'notions/cpp-01' }, { slug: 'notions/cpp-09' }, { slug: 'notions/premieres-expressions' }, { slug: 'notions/premieres-soustractions' }, { slug: 'notions/premieres-multiplications' }, { slug: 'notions/parentheses-calculs' }, { slug: 'notions/premieres-divisions' }, { slug: 'notions/mise-a-jour-compteur' }, { slug: 'notions/premiers-booleens' }, { slug: 'notions/premiere-comparaison' }, { slug: 'notions/atteindre-ou-depasser' }, { slug: 'notions/en-dessous-ou-au-maximum' }, { slug: 'notions/egal-ou-different' }] },
    ],
  })],
});
