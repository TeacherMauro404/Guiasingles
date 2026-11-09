# 1° Medio (A1) — Vocabulario y escritura (cont.)
TEMAS = [
# ------------------------------------------------------------------ JOBS
dict(slug="jobs", titulo="Jobs & Occupations", nivel="1°", cefr="A1",
 objetivo="nombrar profesiones y oficios, y describir lo que hacen y dónde trabajan.",
 goal="talk about jobs, what people do and where they work.",
 recordar=[
  "Con profesiones usamos <b>a / an</b>: <i>She is <b>a</b> nurse. He is <b>an</b> engineer.</i>",
  "Preguntar: <i>What do you do? / What does she do?</i> → <i>She's a cook. She works in a restaurant.</i>",
  "Oficios marítimos: captain, sailor, fisherman, ship's engineer, mechanic, electrician, cook, port worker, diver, navy officer",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the job and the place", instr="Une cada profesión con su lugar de trabajo.", pares=[
   ("a nurse", "in a hospital"), ("a teacher", "in a school"), ("a cook", "in a kitchen"), ("a sailor", "on a ship"), ("a mechanic", "in a garage"),
   ("a shop assistant", "in a shop"), ("a farmer", "on a farm"), ("a pilot", "on a plane")]),
  dict(tipo="fill", titulo="A or AN?", instr="Escribe a o an.", items=[
   "He is [an] electrician.", "She is [a] captain.", "My uncle is [a] fisherman.", "Is she [an] engineer?", "I want to be [a] diver.",
   "He's [an] officer in the navy.", "My mum is [a] doctor.", "She's [an] artist."]),
  dict(tipo="fill", titulo="Who is it?", instr="Escribe la profesión según la descripción.", banco=["firefighter", "mechanic", "cook", "electrician", "captain", "vet", "fisherman", "police officer"], items=[
   "He repairs cars. → [mechanic]", "She prepares food. → [cook]", "He commands a ship. → [captain]", "She works with cables and lights. → [electrician]",
   "He puts out fires. → [firefighter]", "She helps sick animals. → [vet]", "He catches fish. → [fisherman]", "She protects people. → [police officer]"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "What {do|does*} your father do?", "She {work|works*} in a hospital.", "A pilot {flies*|drives} planes.", "My mother is {a|an*} accountant.",
   "They {is|are*} sailors.", "{What*|Where} does he do? — He's a cook.", "A {vet*|dentist} helps animals.", "He {repair|repairs*} engines."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con las palabras del recuadro.", banco=["engineer", "works", "ship", "captain", "engines", "cook", "uniform", "crew"], texto=
   "My brother Felipe is a marine [engineer]. He [works] on a big cargo [ship]. He repairs and checks the [engines]. "
   "The [captain] of the ship is from Norway. There are twenty people in the [crew]. The [cook] prepares food for everybody. "
   "Felipe wears a blue [uniform] and he loves his job."),
  dict(tipo="rewrite", titulo="Write questions and answers", instr="Escribe la pregunta y la respuesta como el ejemplo.", cols=1, items=[
   "your mother / nurse / hospital => What does your mother do? She's a nurse. She works in a hospital.",
   "Pedro / mechanic / garage => What does Pedro do? He's a mechanic. He works in a garage.",
   "your cousins / sailors / ship => What do your cousins do? They're sailors. They work on a ship."]),
  dict(tipo="classify", titulo="Classify the jobs", instr="¿Trabajan en el mar o en tierra?", categorias={
   "AT SEA": ["sailor", "fisherman", "diver", "captain"], "ON LAND": ["teacher", "farmer", "nurse", "shop assistant"]}),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My aunt is a nurse in Valparaíso.", "What does your father do?", "I want to be a ship's engineer.", "She works in a bank."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Jobs at the port", texto=
   "The port of Valparaíso is a busy place. Many people work there. Crane operators move containers from the ships. Port workers check the cargo. "
   "Customs officers control what enters the country. Tug boat captains help big ships to arrive safely. There are also mechanics, electricians and security guards. "
   "Some of them studied at the Instituto Marítimo.",
   vf=[("Crane operators move containers.", True), ("Customs officers cook food.", False), ("Tug boats help big ships.", True), ("There are no mechanics at the port.", False)],
   preguntas=["What do port workers do? => They check the cargo.", "What do customs officers do? => They control what enters the country."]),
  dict(tipo="write", titulo="Your future job", instr="Escribe sobre tu trabajo ideal.", items=[
   "I want to be", "I want to work in / on", "In this job you", "I like this job because"]),
 ]),

# ------------------------------------------------------------------ BODY
dict(slug="body", titulo="Parts of the Body", nivel="1°", cefr="A1",
 objetivo="nombrar partes del cuerpo, describir a personas y hablar de dolencias.",
 goal="name parts of the body and describe people.",
 recordar=[
  "head, hair, face, eye, ear, nose, mouth, tooth/teeth, neck, shoulder, arm, elbow, hand, finger, back, stomach, leg, knee, foot/feet, toe",
  "Describir: <i>She <b>has</b> long hair and brown eyes. He <b>is</b> tall and thin.</i>",
  "Dolencias: <i>I have a headache / a stomachache / a sore throat. My leg hurts.</i>",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the words", instr="Une la palabra con su traducción.", pares=[
   ("shoulder", "hombro"), ("knee", "rodilla"), ("elbow", "codo"), ("neck", "cuello"), ("toe", "dedo del pie"), ("stomach", "estómago"),
   ("teeth", "dientes"), ("back", "espalda")]),
  dict(tipo="fill", titulo="How many?", instr="Escribe el número en palabras y la parte del cuerpo en plural.", items=[
   "I have [two] eyes.", "I have [ten] fingers.", "I have one [nose].", "I have two [feet].", "I have thirty-two [teeth].", "I have two [ears]."]),
  dict(tipo="fill", titulo="What do we use?", instr="Completa con una parte del cuerpo.", items=[
   "We see with our [eyes].", "We hear with our [ears].", "We smell with our [nose].", "We walk with our [legs / feet].",
   "We eat with our [mouth].", "We write with our [hands].", "We think with our [head / brain].", "We chew with our [teeth]."]),
  dict(tipo="classify", titulo="Head or rest of the body?", instr="Clasifica las palabras.", categorias={
   "HEAD / FACE": ["eyebrow", "cheek", "chin", "lips", "forehead"], "REST OF THE BODY": ["wrist", "ankle", "chest", "hip", "thumb"]}),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "She {has*|is} blue eyes.", "He {has|is*} tall.", "I have two {foots|feet*}.", "My {tooth|teeth*} are white.", "I have a {headache*|head hurt}.",
   "My leg {hurt|hurts*}.", "He has {long black hair*|hair long black}.", "She has {a*|an} small nose."]),
  dict(tipo="text", titulo="Describe the people", instr="Completa con palabras del recuadro.", banco=["tall", "hair", "eyes", "beard", "short", "has", "is", "nose"], texto=
   "My grandfather is old but strong. He [is] very [tall]. He has grey [hair] and a long white [beard]. His [eyes] are blue. "
   "My little cousin Amanda is very different. She is [short] and she [has] curly brown hair. She has a small [nose] and a big smile."),
  dict(tipo="match", titulo="At the doctor's", instr="Une el problema con el consejo.", pares=[
   ("I have a headache.", "Take an aspirin and rest."), ("I have a toothache.", "Go to the dentist."), ("I have a sore throat.", "Drink hot tea with honey."),
   ("I have a stomachache.", "Don't eat junk food."), ("My back hurts.", "Don't carry heavy things."), ("I have a cold.", "Stay in bed and keep warm.")]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My sister has long straight hair.", "I have a terrible headache.", "His hands are very big.", "Does your knee hurt?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="The football accident", texto=
   "Last Saturday, Bastián played football with his friends at the beach. He ran very fast and fell. Now his knee hurts and his left ankle is blue. "
   "His mother took him to the hospital. The doctor said: 'Don't play football for two weeks. Put ice on your ankle and keep your leg up.' "
   "Bastián is sad, but he can still use his hands to play video games!",
   vf=[("Bastián played basketball.", False), ("His knee hurts.", True), ("His right ankle is blue.", False), ("He can't play football for two weeks.", True)],
   preguntas=["Who took him to the hospital? => His mother.", "What must he put on his ankle? => Ice."]),
  dict(tipo="write", titulo="Describe a person", instr="Describe a un familiar o personaje famoso (sin decir su nombre).", items=[
   "He / She is", "He / She has … hair", "His / Her eyes are", "He / She also has"]),
 ]),

# ------------------------------------------------------------------ TIME
dict(slug="time", titulo="Telling the Time", nivel="1°", cefr="A1",
 objetivo="preguntar y decir la hora en inglés.",
 goal="ask and tell the time.",
 recordar=[
  "<i>What time is it? / What's the time?</i> → <i>It's …</i>",
  "3:00 three <b>o'clock</b> · 3:15 <b>quarter past</b> three · 3:30 <b>half past</b> three · 3:45 <b>quarter to</b> four",
  "3:10 ten <b>past</b> three · 3:50 ten <b>to</b> four · forma digital: 3:20 → <i>three twenty</i>",
  "<b>at</b> + hora: <i>at seven o'clock</i> · a.m. (mañana) / p.m. (tarde-noche) · midday / midnight",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the time in words", instr="Escribe la hora (forma tradicional).", items=[
   "7:00 → [seven o'clock]", "8:30 → [half past eight]", "2:15 → [quarter past two]", "4:45 → [quarter to five]", "10:10 → [ten past ten]",
   "6:50 → [ten to seven]", "11:20 → [twenty past eleven]", "9:35 → [twenty-five to ten]", "12:00 → [twelve o'clock / midday]", "1:05 → [five past one]"]),
  dict(tipo="fill", titulo="Write the time in numbers", instr="Escribe la hora en números.", items=[
   "half past six → [6:30]", "quarter to nine → [8:45]", "twenty past four → [4:20]", "five to twelve → [11:55]", "quarter past ten → [10:15]", "ten o'clock → [10:00]"]),
  dict(tipo="fill", titulo="Digital time", instr="Escribe la hora en forma digital (ej. 7:25 = seven twenty-five).", items=[
   "7:25 → [seven twenty-five]", "3:40 → [three forty]", "11:15 → [eleven fifteen]", "5:55 → [five fifty-five]", "9:05 → [nine oh five]", "8:30 → [eight thirty]"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "4:30 = {half past four*|half past five}", "7:45 = {quarter past seven|quarter to eight*}", "School starts {at*|in|on} 8:00.",
   "{What*|How} time is it?", "It's {three o'clock*|three hours}.", "10:50 = {ten to eleven*|ten past eleven}"]),
  dict(tipo="text", titulo="Complete the timetable text", instr="Escribe las horas en palabras.", texto=
   "On weekdays, I get up at [quarter past six] (6:15). I take the bus at [seven o'clock] (7:00). Classes start at [eight o'clock] (8:00). "
   "We have a break at [quarter to ten] (9:45) and lunch at [half past one] (1:30). School finishes at [twenty past four] (4:20). "
   "I go to bed at [half past ten] (10:30)."),
  dict(tipo="rewrite", titulo="Answer the questions", instr="Responde con oraciones completas.", cols=2, items=[
   "What time do you get up? => I get up at …", "What time do you have lunch? => I have lunch at …", "What time does school start? => It starts at …",
   "What time do you go to bed? => I go to bed at …"]),
  dict(tipo="match", titulo="Match the clocks", instr="Une la hora en palabras con la hora digital.", pares=[
   ("twenty-five past six", "6:25"), ("quarter to three", "2:45"), ("half past eleven", "11:30"), ("ten to nine", "8:50"),
   ("five past four", "4:05"), ("quarter past seven", "7:15"), ("twenty to one", "12:40"), ("midnight", "00:00")]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "What time is it, please?", "It's half past nine.", "The ferry leaves at quarter past three.", "I have English at ten o'clock."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el horario y responde.", titulo_texto="Ferry timetable: Valparaíso – Juan Fernández (one day)", texto=
   "Boarding: 6:45 · Departure: 7:00 · Breakfast on board: 7:30 – 8:30 · Safety drill: 9:15 · Lunch: 12:30 · Arrival: 5:40 p.m.",
   preguntas=["What time does the ferry leave? => At seven o'clock.", "When is breakfast? => From half past seven to half past eight.",
              "What time is the safety drill? => At quarter past nine.", "What time does it arrive? => At twenty to six (p.m.)."]),
  dict(tipo="write", titulo="Your daily timetable", instr="Escribe tu horario con horas en palabras.", items=[
   "I wake up at", "I have breakfast at", "I arrive at school at", "I do my homework at"]),
 ]),

# ------------------------------------------------------------------ PERSONAL INFORMATION
dict(slug="personal-information", titulo="Personal Information", nivel="1°", cefr="A1",
 objetivo="presentarse y dar información personal básica de forma oral y escrita.",
 goal="introduce yourself and give personal information.",
 recordar=[
  "<i>My name is … · I'm … years old. · I'm from … · I live in … · My phone number is … · My e-mail is …</i>",
  "Preguntas: <i>What's your name? · How old are you? · Where are you from? · Where do you live? · What's your surname? · How do you spell it?</i>",
  "Deletreo: A (ei) · E (i) · I (ai) · G (yi) · J (yei) · @ = at · . = dot",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match questions and answers", instr="Une cada pregunta con su respuesta.", pares=[
   ("What's your name?", "My name is Ignacio."), ("How old are you?", "I'm fifteen."), ("Where are you from?", "I'm from Chile."),
   ("Where do you live?", "I live in Cerro Barón."), ("What's your phone number?", "It's 9 8765 4321."), ("How do you spell your surname?", "R-O-J-A-S."),
   ("What's your favourite subject?", "English, of course!"), ("When is your birthday?", "On 4th June.")]),
  dict(tipo="fill", titulo="Complete the questions", instr="Completa con la palabra correcta.", items=[
   "[What]'s your name?", "How [old] are you?", "Where are you [from]?", "Where do you [live]?", "What's your [e-mail] address?",
   "How do you [spell] that?", "[When] is your birthday?", "What [do] you like doing?"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I {am*|have} fifteen years old.", "I {live*|lives} in Valparaíso.", "My name {is*|are} Daniela.", "I'm {from*|of} Chile.",
   "My e-mail is ana{@|at*}gmail.com (spoken)", "My {surname*|name last} is González."]),
  dict(tipo="text", titulo="Complete the introduction", instr="Completa con las palabras del recuadro.", banco=["name", "years", "from", "live", "brothers", "favourite", "like", "want"], texto=
   "Hello! My [name] is Vicente Araya. I'm fifteen [years] old. I'm [from] Chile and I [live] in Viña del Mar with my parents and two [brothers]. "
   "My [favourite] subject is Mechanics. I [like] playing football and listening to music. In the future, I [want] to work on a ship."),
  dict(tipo="fill", titulo="Complete the form", instr="Lee el texto anterior y completa la ficha de Vicente.", cols=1, items=[
   "First name: [Vicente]", "Surname: [Araya]", "Age: [15]", "City: [Viña del Mar]", "Favourite subject: [Mechanics]", "Hobbies: [football and music]"]),
  dict(tipo="rewrite", titulo="Write the questions", instr="Escribe la pregunta para cada respuesta.", cols=2, items=[
   "I'm sixteen. => How old are you?", "I'm from Peru. => Where are you from?", "My name is Lucas. => What's your name?",
   "I live in Quilpué. => Where do you live?", "It's on 2nd May. => When is your birthday?", "I like swimming. => What do you like doing?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My surname is Fuentes.", "I live with my grandparents.", "How do you spell your name?", "My favourite subject is English."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el perfil y responde.", titulo_texto="New student profile", texto=
   "Hi everyone! I'm Rayén Huenchumilla. I'm sixteen years old and I'm from Temuco, but now I live in Valparaíso with my aunt. "
   "My surname is Mapuche; you spell it H-U-E-N-C-H-U-M-I-L-L-A. I love the sea and I want to be a navy officer. "
   "My hobbies are reading and swimming. My favourite food is sopaipillas!",
   vf=[("Rayén is fifteen.", False), ("She is from Temuco.", True), ("She lives with her parents.", False), ("She wants to be a navy officer.", True)],
   preguntas=["Who does she live with? => With her aunt.", "What are her hobbies? => Reading and swimming."]),
  dict(tipo="write", titulo="Introduce yourself", instr="Escribe un párrafo de presentación personal (6 oraciones).", items=[
   "My name is", "I'm … years old and I'm from", "I live in … with", "My favourite subject is", "I like", "In the future I want to"]),
 ]),
]
