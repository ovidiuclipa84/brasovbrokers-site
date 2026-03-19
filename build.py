
with open('/Users/ovidiu/Downloads/Claude/website/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

track_record_section = '''
<!-- TRACK RECORD -->
<section id="track-record">
  <div class="section-label">Portofoliu demonstrabil</div>
  <h2>Complexitate asumata,<br>rezultate masurabile</h2>
  <p class="section-intro">Specializarea nu inseamna volum Ñ inseamna capacitatea de a structura corect riscuri pe care putini brokeri le inteleg. Cifrele de mai jos reprezinta proiecte reale, plasate si gestionate integral.</p>

  <div class="track-grid">
    <div class="track-card reveal">
      <div class="track-amount">EUR 180M</div>
      <div class="track-domain">Infrastructura Energie &amp; Constructii</div>
      <div class="track-detail">CAR/EAR, conducte gaze, centrale electrice, instalatii industriale. Plasamente multi-asigurator cu raspundere fata de terti pe santier.</div>
    </div>
    <div class="track-card reveal">
      <div class="track-amount">EUR 40M</div>
      <div class="track-domain">Cogenerare Industriala</div>
      <div class="track-detail">Property All Risks + Machinery Breakdown + Business Interruption. Clauze speciale raspundere producator, furnizor si mentenanta.</div>
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
      <div class="track-detail">Garantii complexe buna executie, avans, participare licitatie. Clauze FIDIC, instrumente hibride de garantare pentru contracte publice majore.</div>
    </div>
  </div>

  <div class="track-total reveal">
    <span class="track-total-label">Total sume asigurate demonstrate</span>
    <span class="track-total-amount">EUR 345M+</span>
  </div>
</section>

'''

# Insert before contact section
content = content.replace('<!-- CONTACT -->', track_record_section + '<!-- CONTACT -->')

# Fix nav to include track-record
content = content.replace(
    '<a href="#contact">Contact</a>',
    '<a href="#track-record">Portofoliu</a><a href="#contact">Contact</a>'
)

# Fix email - plain text no link
old_email = '<div class="contact-detail-val"><span id="cemail"></span></div><script>(function(){var a=document.getElementById("cemail");var l=document.createElement("a");l.href=["m","a","i","l","t","o",":","o","f","f","i","c","e","@","b","r","a","s","o","v","b","r","o","k","e","r","s",".","r","o"].join("");l.textContent=["o","f","f","i","c","e","@","b","r","a","s","o","v","b","r","o","k","e","r","s",".","r","o"].join("");a.appendChild(l);})();</script>'

if old_email in content:
    content = content.replace(old_email, '<div class="contact-detail-val">office@brasovbrokers.ro</div>')
    print('Email inlocuit OK')
else:
    print('Email - cautam varianta alternativa')
    # find line with contact-detail-val and email
    import re
    matches = [(m.start(), content[m.start():m.start()+200]) for m in re.finditer(r'contact-detail-val.*?email|email.*?contact-detail-val', content, re.DOTALL)]
    for pos, txt in matches[:3]:
        print(f'  {pos}: {txt[:100]}')

with open('/Users/ovidiu/Downloads/Claude/website/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fisier salvat OK')
print(f'Dimensiune noua: {len(content)} caractere')
