# -*- coding: utf-8 -*-
with open('/Users/ovidiu/Downloads/Claude/website/index.html', 'r', encoding='utf-8') as fh:
    content = fh.read()

track_css = '''
    /* TRACK RECORD */
    #track-record { padding: 6rem 2rem; max-width: 1100px; margin: 0 auto; text-align: center; }
    .track-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin: 0 auto 3rem; }
    @media (max-width: 860px) { .track-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 540px) { .track-grid { grid-template-columns: 1fr; } }
    .track-card { background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08); border-radius: 12px; padding: 2rem 1.5rem; text-align: left; transition: border-color .3s, transform .3s; }
    .track-card:hover { border-color: rgba(255,255,255,.2); transform: translateY(-4px); }
    .track-amount { font-size: 1.8rem; font-weight: 600; font-family: 'Cormorant Garamond', serif; color: #fff; margin-bottom: .4rem; }
    .track-domain { font-size: .8rem; text-transform: uppercase; letter-spacing: .12em; opacity: .5; margin-bottom: .8rem; }
    .track-detail { font-size: .9rem; line-height: 1.6; opacity: .7; }
    .track-total { display: inline-flex; align-items: center; gap: 1.5rem; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.15); border-radius: 100px; padding: 1rem 2.5rem; margin-top: 1rem; }
    .track-total-label { font-size: .85rem; text-transform: uppercase; letter-spacing: .1em; opacity: .5; }
    .track-total-amount { font-size: 1.6rem; font-weight: 600; font-family: 'Cormorant Garamond', serif; }
'''

track_section = '''
<!-- TRACK RECORD -->
<section id="track-record">
  <div class="section-label">Portofoliu demonstrabil</div>
  <h2>Complexitate asumata,<br>rezultate masurabile</h2>
  <p style="max-width:640px;margin:0 auto 3rem;opacity:.7;font-size:1.05rem;line-height:1.7;">Specializarea nu inseamna volum. Inseamna capacitatea de a structura corect riscuri pe care putini brokeri le inteleg. Cifrele de mai jos reprezinta proiecte reale, plasate si gestionate integral.</p>
  <div class="track-grid">
    <div class="track-card reveal">
      <div class="track-amount">EUR 180M</div>
      <div class="track-domain">Infrastructura Energie &amp; Constructii</div>
      <div class="track-detail">CAR/EAR, conducte gaze, centrale electrice, instalatii industriale. Plasamente multi-asigurator cu raspundere fata de terti pe santier.</div>
    </div>
    <div class="track-card reveal">
      <div class="track-amount">EUR 40M</div>
      <div class="track-domain">Cogenerare Industriala</div>
      <div class="track-detail">Property All Risks + Machinery Breakdown + Business Interruption cu clauze speciale raspundere producator, furnizor si mentenanta.</div>
    </div>
    <div class="track-card reveal">
      <div class="track-amount">EUR 20M/an</div>
      <div class="track-domain">Utilitati Energie</div>
      <div class="track-detail">Property All Risks + Business Interruption pentru producatori de energie electrica. Parteneriate multi-anuale cu reinnoire anuala.</div>
    </div>
    <div class="track-card reveal">
      <div class="track-amount">EUR 15M</div>
      <div class="track-domain">Infrastructura Aeroportuara</div>
      <div class="track-detail">Property All Risks cu 18 peril-uri asigurate. Structura complexa cu clauze specifice infrastructurii critice de transport aerian.</div>
    </div>
    <div class="track-card reveal">
      <div class="track-amount">EUR 11.5M</div>
      <div class="track-domain">Aviatie Comerciala</div>
      <div class="track-detail">Hull + TPL conform London Aviation Market. Clauze AVN52E, AVN85 NCBOR, AVN28B. Expertiza rara in piata romaneasca de brokeraj.</div>
    </div>
    <div class="track-card reveal">
      <div class="track-amount">EUR 70M+</div>
      <div class="track-domain">Garantii Contractuale Publice</div>
      <div class="track-detail">Garantii complexe buna executie, avans si participare licitatie. Clauze FIDIC si instrumente hibride pentru contracte publice majore.</div>
    </div>
  </div>
  <div class="track-total reveal">
    <span class="track-total-label">Total sume asigurate demonstrate</span>
    <span class="track-total-amount">EUR 345M+</span>
  </div>
</section>

'''

content = content.replace('</style>', track_css + '
    </style>')
content = content.replace('<!-- CONTACT -->', track_section + '<!-- CONTACT -->')
content = content.replace('<a href="#contact">Contact</a>', '<a href="#track-record">Portofoliu</a><a href="#contact">Contact</a>')

lines = content.split('
')
for i, line in enumerate(lines):
    if 'contact-detail-val' in line and ('@' in line or 'cemail' in line):
        lines[i] = '        <div class="contact-detail-val">office@brasovbrokers.ro</div>'
        print('Email fix la linia ' + str(i+1))
        break
content = '
'.join(lines)

with open('/Users/ovidiu/Downloads/Claude/website/index.html', 'w', encoding='utf-8') as fh:
    fh.write(content)

print('DONE - ' + str(len(content)) + ' chars')
