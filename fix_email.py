with open('/Users/ovidiu/Downloads/Claude/website/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_line = '        <div class="contact-detail-val"><a id="cemail" href="#">office@brasovbrokers.ro</a></div><script>var e=document.getElementById("cemail");e.href=["mai","lto:","office","@brasovbrokers.ro"].join("");</script>' + chr(10)

lines[664] = new_line

with open('/Users/ovidiu/Downloads/Claude/website/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('OK - linia 665 actualizata')
