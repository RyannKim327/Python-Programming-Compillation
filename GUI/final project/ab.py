import requests
import json

quotes = [
	"Ang edukasyon ay hindi lamang bilang pagtanggap nang isang papel, kundi ito ay ang natutunan at karunungan na nakukuha mo nang may pagsisikap.",
	"Minsan, batid na natin ang katotohanan, subalit, tayo na mismo ang hindi tumatanggap nito.",
	"Oras ang isang bagay na kahit kailan ay hindi mo na maaari pang ibalik.",
	"Ang buhay ay parang isang awit, mayroong melodiya na siyang gumagabay sa kung paano ba mabuhay.",
	"Ang pagiging mapag isa ay hindi masamang gawain, kundi ito ay ang mga nasa paligid mo na nanloloko sa iyo.",
	"Huwag kang matakot na magkamali, dahil diyan ka uunlad at matututo.",
	"Wala ni isa ang magiging pinakamahusay na guro, kundi ang buhay at ang buhay ay ang Diyos.",
	"Huwag na huwag mong ikukumpara ang sarili mo sa iba, dahil ikaw ay naiiba sa lahat.",
	"Ang kaligayahan ay isang bagay na bumubulag sa tunay at katotohanan.",
	"Mas mainam pang maging mapag isa, kaysa sa kasama mo ang iba.",
	"Pananampalataya, kay gandang salita. Isang salitang magbibigay nang lakas upang mabuhay.",
	"Bakit kaya maraming awitin ang malulungkot at kapighatian, gayong maraming tao rin naman ang ginusto, subalit hindi minahal.",
	"Ang pag ibig ay iba sa pagkagusto. Kaya huwag mong sabihin sa isang taong mahal mo siya, kung sa isang banda ay gusto mo lang siya.",
	"Ang pag ibig ay isang nakakabighaning salita, na siya ring wawasak nang iyong buhay.",
	"Ngiti, marami sa atin ang maraming pinagdadaanan, subalit ang pagngiti ay makakatulong upang mapagaan lahat nang bagay.",
	"Huwag ninyong ipaalam sa kahit na sino kung sino nga ba talaga ako, bagkus ipakilala nyo ako sa kanila sa paraang kung paano nyo ako nakilala.",
	"Ang kanang kamay ko ay hindi kasing buti nang kung ano ang nasa isip mo.",
	"Huminga ka nang malalim, isipin mo, sapat pa ba sa akin ang maging kabilang dito.",
	"Pwede mo akong husgahan ay sirain ang aking buhay, subalit mag iingat ka na sa mga susunod mong hakbang.",
	"Maaaring malaman nang mga tao ang aking pangalan, nguti hindi ang aking pagkakakilanlan.",
	"Parati kong hinahamon ang katangahan nang lipunan, kung saan maraming mga taong hindi panatag, subalit bulgaran kung magpakilala.",
	"Palagi kong tinatawanan ang mga pagdududa, dahil sa parati nilang inihahambing ang kanilang sarili sa mga walang kwentang tao.",
	"Wala akong pake kung galit ka man sa akin, dahil sa una pa lang, hindi naman kita kilala.",
	"Hanapin ninyo ako sa talaan nang hanapan, at makikita nyo ang mga patungkol sa akin na walang katotohanan.",
	"Ito nga ba ang pangalan ko. Gaano ka kasigurado.",
	"Ang mundong ito ay akin lamang kalaro, at isa ka sa mga piyesa na ginagamit naming dalawa.",
	"Kung kaya mong sagutan ang palaisipan, mauunawaan mo at malalaman kung ano ang sinasambit ko.",
	"Ang pinakamalaking kalokohang lumalaganap, ay kagagawan nang tao.",
	"Kung nais mong mahusgahan, ako ay husgahan mo at gagawin ko sa iyo ang kung anong ginawa mo.",
	"Ang mga taong banal kuno, maraming alam patungkol sa bibliya, subalit hindi kayang isabuhay ay isang uri nang hipokrito sa akin.",
	"Tanging salamin lamang ang isang bagay na ni minsan ay hindi kayang magsinungaling.",
	"Pwede kang mameke nang ngiti, na siya ring papaslang sa iyo.",
	"Ang kalangitan ay isang lugar kung saan matatanaw ang kasinungalingan nang maling katotohanan.",
	"Bakit ang isang araw ay parating inihahambing sa buhay. Dahil ang kamatayan ang katotohanan at ang buhay ay isang kasinungalingan nang lahat dito sa lupa.",
	"Ako ay tumatayo sa isang lugar kung saan walang nakakakita sa akin.",
	"Parati akong humihiwalay sa lahat, hindi dahil sa hindi ko sila kailangan, bagkus ayaw ko lang na parati akong umaasa sa kanila.",
	"Parating pakinggan ang sarili, kausapin at kung anong sabihin ay gawin. Subalit, kung sinabi ay magpakamatay, pag isipan mo nang tatlong beses.",
	"Palagi akong naglalaro sa mga petsa at bilang na para bang naganap na sa nakaraan ko.",
	"May nagustuhan akong tao, na siya ring sahilan kung kaya pa at ayaw ko nang magkagusto pa sa iba.",
	"Kung gusto mo lang ang isang tao, at hindi mo naman mahal, huwag mo munang ituloy, bagkus, kilalanin nyo muna ang isat isa.",
	"Hindi ko kailangan nang taong maawain, bagkus, mas kailangan ko iyong taong sisisihin pa ako."
]

file = open("a.txt", "w")

a = ""

for i in quotes:
	out = json.loads(requests.get(f"https://api-baybayin-transliterator.vercel.app/?text={i}").text)['baybay']
	print(out)
	a += f"\"{out}\",\n"

print(a)

file.write(a)