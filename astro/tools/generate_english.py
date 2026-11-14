"""Regenerate English pages after updating the Swedish presentation or translations."""
from pathlib import Path
p=Path(__file__).resolve().parents[1]
translations={
'Nu / Ghana':'Now / Ghana',
'En pilot i praktiken.':'A pilot in practice.',
'Solvinter arbetar med en liten grupp deltagare i Ghana för att undersöka hur Eira, praktiska uppgifter och gemensam reflektion kan stödja lärande och skapande.':'Solvinter is working with a small group of participants in Ghana to explore how Eira, practical assignments and shared reflection can support learning and creative work.',
'Deltagandet är tills vidare begränsat medan formen prövas och förbättras.':'Participation remains limited while the format is tested and improved.',
'Läs om Eira':'Read about Eira',
'En aktiv pilot, tillsammans med långsiktiga projekt under utveckling.':'One active pilot, alongside longer-term projects in development.',
'Planerat projekt':'Planned project',
'Aktiv pilot':'Active pilot',
'Publicerat':'Published',

'Urvalet är fastställt av fotografen.':'The selection is the photographer’s.',
'Om Solvinter':'About Solvinter',
'Solvinter är ett oberoende initiativ som verkar inom medicin, artificiell intelligens, filosofi och konst.':'Solvinter is an independent initiative working across medicine, artificial intelligence, philosophy and the arts.',
'Grundat av Dominic Eriksson Giwa, en svensk läkare som utforskar mötet mellan mänsklig kunskap och framväxande teknologier.':'Founded by Dominic Eriksson Giwa, a Swedish physician exploring the intersection of human knowledge and emerging technologies.',
'Solvinter på GitHub (öppnas i ny flik)':'Solvinter on GitHub (opens in a new tab)',
'Kontakt':'Contact',

'Medicin, AI och bioteknik samlas här: från utvärdering av medicinska AI-system till forskning och rådgivning.':'Medicine, AI and biotechnology come together here: from evaluating medical AI systems to research and consultation.',
'Områden':'Areas',
'Första föreslagna arbetsprovet är en avgränsad utvärdering med bedömningsmatris, felanalys och rapport.':'The first proposed work sample is a focused evaluation with an assessment framework, error analysis and report.',
'Projektpresentation under utveckling.':'Project presentation in development.',
'Medicinsk forskning, litteraturöversikter och AI-stödda forskningsflöden.':'Medical research, literature reviews and AI-assisted research workflows.',
'Rådgivning kring medicinsk AI och forskningsarbete. Omfattning och uppdragsvillkor utvecklas.':'Consultation on medical AI and research. Scope and terms of engagement are in development.',
'En plats för AI-genererade konstnärliga arbeten. Presentation förbereds.':'A place for AI-generated artistic work. A presentation is being prepared.',

'Öppna data, AI och ekonomisk analys för att identifiera möjligheter.':'Open data, AI and economic analysis to identify opportunities.',
'Sol 1 / Beräkningsresurs':'Sol 1 / Compute resource',
'Lokal AI och GPU-beräkningar.':'Local AI and GPU computing.',
'Sol 1 är en lokal arbetsstation med NVIDIA RTX 4090 och 24 GB grafikminne, avsedd för prototyper, utvärdering och utvalda arbetsflöden med lokala modeller inom Solvinter. Det är en intern resurs, inte en publik molntjänst, och extern åtkomst erbjuds inte i nuläget.':'Sol 1 is a local workstation with an NVIDIA RTX 4090 and 24 GB of VRAM, intended for prototyping, evaluation and selected local-model workloads within Solvinter. It is an internal resource, not a public cloud service, and external access is not currently offered.',
'Sol 1 · Hårdvara':'Sol 1 · Hardware',
'Kärnor / trådar':'Cores / threads','Maxfrekvens':'Maximum frequency','L3-cache':'L3 cache','Grafikkort':'Graphics card','Grafikminne':'VRAM','Operativsystem':'Operating system','5,05 GHz':'5.05 GHz',

'Lokal förhandsversion · design och innehåll för granskning':'Local preview · design and content for review',
'En oberoende ateljé · Solvinter':'An independent atelier · Solvinter',
'Att se närmare.':'Look closer.', 'Att tänka vidare.':'Think further.',
'En växande plats för medicin, filosofi, AI och konst. För frågor som behöver tid, och idéer som förtjänar att bli till.':'A growing place for medicine, philosophy, AI and art. For questions that need time, and ideas worth bringing into being.',
'Utforska arbetet':'Explore the work',
'Strand i varmt kvällsljus, ur Dominics Ghana-urval':"Beach in warm evening light, from Dominic’s Ghana selection",
'Ur bildarkivet / Ghana':'From the photographic archive / Ghana',
'Dominic Eriksson Giwa · ur ghana_selection':'Dominic Eriksson Giwa · from ghana_selection',
'01 / Utgångspunkt':'01 / Starting point','Mellan kunskap':'Between knowledge','och föreställningsförmåga.':'and imagination.',
'Solvinter tar form i mötet mellan vetenskapligt undersökande och konstnärligt arbete. Här får texter, fotografier och tekniska experiment utvecklas i sin egen takt.':'Solvinter takes shape where scientific inquiry meets artistic practice. Here, writing, photography and technical experiments can develop at their own pace.',
'Initiativet drivs av Dominic Eriksson Giwa, med bakgrund som läkare och intressen inom filosofi, AI, bioteknik och konst.':'The initiative is led by Dominic Eriksson Giwa, whose background is in medicine and whose interests span philosophy, AI, biotechnology and art.',
'Frågor i arbete.':'Questions in progress.',
'Presentation under utveckling':'Presentation in development',
'69 fotografier från Ghana. Ett konstnärligt urval av Dominic Eriksson Giwa, samlat i Collection 001.':'69 photographs from Ghana. An artistic selection by Dominic Eriksson Giwa, brought together in Collection 001.',
'Urvalet är fastställt av fotografen. Presentationen granskas lokalt före publicering.':'The selection is the photographer’s. The presentation is being reviewed locally before publication.',
'Se samlingen · jämför tre layouter':'View the collection · compare three layouts',
'Litterärt arbete. Presentation förbereds under Art.':'A literary work. A presentation is being prepared under Art.',
'Tanke får ta plats.':'Room for thought.',
'Filosofi, medicin, psykiatrisk nosologi, AI och vetenskapsteori. Här ska färdigställda och granskade essäer samlas.':'Philosophy, medicine, psychiatric nosology, AI and the philosophy of science. This will be a home for completed and reviewed essays.',
'Den första publiceringen förbereds.':'The first publication is being prepared.',
'Innan det är klart.':'Before it is ready.',
'Ateljén rymmer pågående arbeten, skisser och experiment. Just nu bygger vi grunden för bildarkivet och Collection 001.':'The atelier holds work in progress, sketches and experiments. We are currently building the foundations for the photographic archive and Collection 001.',
'Det privata urvalsverktyget körs separat lokalt. Bilder och beslut stannar på datorn.':'The private selection tool runs separately on the local computer. Images and decisions stay on the device.',
'Medicinsk kunskap.':'Medical knowledge.','Nya verktyg.':'New tools.',
'Tjänsteerbjudande under utveckling för forskningsnära och medicinska uppdrag.':'Services in development for medical and research-related assignments.',
'Första föreslagna arbetsprovet: en avgränsad utvärdering av ett medicinskt AI-system med bedömningsmatris, felanalys och rapport. Kontaktuppgifter och uppdragsvillkor läggs till efter granskning.':'First proposed work sample: a focused evaluation of a medical AI system, including an assessment framework, error analysis and report. Contact details and terms will be added after review.',
'Ett tjänsteerbjudande för utvärdering av medicinska AI-system utvecklas.':'A service for evaluating medical AI systems is in development.',
'En AI-guide för att lära genom att göra, nu i en liten pilot i Ghana genom Solvinter Tech.':'A guided AI companion for learning by doing, now being tested in a small Ghana pilot through Solvinter Tech.',
'Medicin, metabolism och bioteknologisk utveckling.':'Medicine, metabolism and biotechnology development.',
'Lokal presentation · ännu inte publicerad':'Local preview · not yet published',
'69 fotografier från Ghana. Urval och fotografi av Dominic Eriksson Giwa.':'69 photographs from Ghana. Photography and selection by Dominic Eriksson Giwa.',
'Platser, människor och spår av liv.':'Places, people and traces of life.',
'Fotografi & urval':'Photography & selection', '69 fotografier':'69 photographs', 'Ur fotografens egen samling':'From the photographer’s own collection',
'Välj layout':'Choose a layout','Bildrytm':'Visual rhythm','Galleri':'Gallery','Tidskrift':'Editorial','Kontaktkarta':'Contact sheet',
'Beskär till gemensamma ramar':'Crop to matching frames',
'Bildrytm — täta rader med växlande höjd. Färg möter sammanhållna svartvita avsnitt.':'Visual rhythm — closely spaced rows of varying height. Colour alternates with coherent black-and-white passages.',
'Galleri — stora bilder, generösa mellanrum och fotografiernas egna proportioner.':'Gallery — large images, generous spacing and the photographs’ original proportions.',
'Tidskrift — växlande storlek, asymmetri och parvisa möten. Beskärning kan slås på som ett separat förslag.':'Editorial — varied sizes, asymmetry and paired images. Cropping can be enabled as a separate presentation option.',
'Kontaktkarta — en överblick med samma ordning och hela bildytan synlig.':'Contact sheet — an overview in the same order, with every image shown in full.',
'Samma 69 fotografier i alla förslag. Föreslagen sekvens i färg och svartvitt; bildytorna visas i sin helhet.':'The same 69 photographs in every layout. A proposed sequence in colour and black and white; images are shown in full.',
'Ghana, alla 69 fotografier':'Ghana, all 69 photographs',
'Öppna fotografi ':'Open photograph ', ' i sin helhet':' in full',
'Slut på samlingen / 69 fotografier':'End of the collection / 69 photographs',
'Ett urval. Flera sätt att se.':'One selection. Different ways of seeing.',
'Bildurvalet förblir fotografens. Layout och bildrytm är presentationsförslag.':'The selection remains the photographer’s. Layout and rhythm are presentation proposals.',
'Till början':'Back to top','Färg':'Colour','Svartvitt':'Black and white',
'← Alla projekt':'← All projects',
}
def translate(s):
 # Replace longest phrases first; escaped curly quotes keep JavaScript strings valid.
 for sv,en in sorted(translations.items(),key=lambda item:-len(item[0])):s=s.replace(sv,en)
 return s
for file in ['index.astro','art/collection-001.astro','projects/[id].astro']:
 s=(p/'src/pages'/('sv/index.astro' if file=='index.astro' else file)).read_text()
 s=translate(s)
 # One additional route directory requires one additional parent in imports.
 if file!='index.astro':s=s.replace("from '../","from '../../")
 s=s.replace('href="/sv/#projects"','href="/en/#projects"').replace('href="/art/collection-001/"','href="/en/art/collection-001/"').replace('href="/projects/eira/"','href="/en/projects/eira/"')
 s=s.replace("href={'/projects/'+p.id+'/'}","href={'/en/projects/'+p.id+'/'}")
 if file=='index.astro':
  descriptions={k:translations[k] for k in ['Ett tjänsteerbjudande för utvärdering av medicinska AI-system utvecklas.','En AI-guide för att lära genom att göra, nu i en liten pilot i Ghana genom Solvinter Tech.','Medicin, metabolism och bioteknologisk utveckling.','Öppna data, AI och ekonomisk analys för att identifiera möjligheter.']}
  import json
  s=s.replace("const projects=await getCollection('projects');", "const projectTranslations="+json.dumps(descriptions,ensure_ascii=False)+";\nconst projects=(await getCollection('projects')).map(p=>({...p,data:{...p.data,description:projectTranslations[p.data.description]||p.data.description}}));")
 if file=='projects/[id].astro':
  s=s.replace('<Content/>',"{entry.id==='observatory'?<><p>Solvinter Observatory is a planned project for identifying opportunities by combining open data, AI and economic analysis. The observatory is open to a range of applications.</p><h3>Compute Economics</h3><p>The first planned application is Compute Economics: tracking GPU prices, mining revenue and rental markets to identify differences in profitability.</p><p>The project is at the idea stage. Data collection and ongoing monitoring are not yet operational.</p></>:entry.id==='eira'?<><p>Eira is a guided AI companion for learning by doing: understanding an assignment, asking questions, solving one problem at a time and reflecting on what comes next.</p><p>A small, limited pilot is underway with participants in Ghana. The wider product remains under development, and access is not generally open.</p></>:<><p>{{metabolismx:'Medicine, metabolism and biotechnology development.','clinical-ai':'A service for evaluating medical AI systems is in development.'}[entry.id]}</p><p>This is a planned project. Scope, status and work samples will be reviewed before publication.</p></>}")
 if file=='art/collection-001.astro':s=s.replace('alt={photo.alt}',"alt={'Ghana, photograph '+photo.id+' from Dominic Eriksson Giwa’s selection'}")
 dest=p/'src/pages/en'/file;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(s)
 if file=='index.astro':
  (p/'src/pages/index.astro').write_text(s.replace("from '../../","from '../"))
print('Generated English homepage, collection and project routes.')
