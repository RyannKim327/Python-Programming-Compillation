import requests

b = "-i-" + "\n"
b += "Linihim mo ang gawang, sa iba'y malabong matupad" + "\n"
b += "kahilingan at hangad, piunagkaloob ng tapat" + "\n"
b += "Sapat nang masilayan kang ganyan, kahit sa loob ng tahanan" + "\n"
b += "At ang bawat gawa mong nag-iiba, lubbos kong kinalulugdan" + "\n"

b += "\n"
b += "-ii-" + "\n"
b += "Sa tuwing nababatid, sarili'y kinukublli" + "\n"
b += "Sa kadahilanang, may pag-asang 'di mawari" + "\n"
b += "Sa oras mang dumating, aking lubos na masasabi" + "\n"
b += "Salamat sapagkat, lubos ang binigay mong ngiti" + "\n"

b += "\n"
b += "-iii-" + "\n"
b += "Noong tangan mo sa bisig, ang isang tulad ko" + "\n"
b += "Lubos na ipagpapasalamat, sapagkat tunay ngang totoo" + "\n"
b += "Hindi mawari ng kung sinuman, ang ngiting nasa labi ko" + "\n"
b += "Dahil sa ika'y mahal ko, higit pa sa kung sino ako" + "\n"

b += "\n"
b += "-iv-" + "\n"
b += "Ikaw nga ang haligi, at pinatunayan mo sa akin" + "\n"
b += "Ang respeto at paggalang, na syang dapat ipataw galing sa amin" + "\n"
b += "Nawa isang araw, kasamana ka sa iglesyang sambahayan" + "\n"
b += "Kung saan ang Amang nasa langit, sabay sabay nating papurihan" + "\n"

b += "\n"
b += "-v-" + "\n"
b += "Nilikha nya ang langit, lupa at karagatan" + "\n"
b += "Subalit sa lahat ng nilikha, kayo ang lubos kong inaasam" + "\n"
b += "Na kaniyang nilikhang, 'di ko nais lumisan" + "\n"
b += "Gayong pinipilit kong lubos, dahil sa lubos ko ring pinagsisisihan" + "\n"

b += "\n"
b += "-vi-" + "\n"
b += "Wala man akong naiambag, sa kapatid na lumisan" + "\n"
b += "Nais ko namang ika'y, nasa langit na kaharian" + "\n"
b += "Upang masaksihan ang lahat, maging ang kaginhawahan" + "\n"
b += "Maibsan ang dating paghihirap, maging naging kapighatian" + "\n"

b += "\n"
b += "-vii-" + "\n"
b += "Saksi kaming mga anak mo, kung paano kang nagluksa" + "\n"
b += "Isa ba iyon sa simula, kaya nagbabalak bumalik sa kanya" + "\n"
b += "Nais ko sanang tuluyan kang magbago, ama ko sa laman at lupa" + "\n"
b += "Na syang dahilan, kung bakit ako nakatapak sa lupa" + "\n"

b += "\n"
b += "-viii-" + "\n"
b += "Noong ika'y laging galit, ngayo'y mapag-unawa na" + "\n"
b += "Saksi sa pagbabago mong, tila isang malaki ring himala" + "\n"
b += "Gayong isang bagay na tila, aking pinagsisihang talaga" + "\n"
b += "At iyo'y makasama ka, sa araw na kasama ka nila"

a = requests.post("https://poem.writers.repl.co/compose", json={
    "author": "19N0R3",
    "title": "Dati sa Ngayon",
    "content": b,
    "password": "223244245401009469800406802567671183911671827129"
})

print(a.text)