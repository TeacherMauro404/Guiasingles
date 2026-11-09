# 2° Medio (A2) — Gramática, parte B
TEMAS = [
# ------------------------------------------------------------------ LIKES & GERUNDS
dict(slug="likes-gerunds", titulo="Likes & Dislikes + Gerunds", nivel="2°", cefr="A2",
 objetivo="expresar gustos y preferencias con love / like / enjoy / don't mind / hate + verbo-ing.",
 goal="talk about likes and dislikes using verb + -ing.",
 recordar=[
  "<b>love</b> (++) · <b>like / enjoy</b> (+) · <b>don't mind</b> (0, me da igual) · <b>don't like</b> (-) · <b>hate / can't stand</b> (- -, no soporto)",
  "Después de estos verbos usamos <b>verbo + -ing</b>: <i>I enjoy <b>swimming</b>. She hates <b>getting up</b> early.</i>",
  "Preguntar: <i>Do you like dancing? — Yes, I do. / What do you like doing? — I like reading.</i>",
  "También: <i>I'm good at <b>cooking</b>. I'm interested in <b>sailing</b>.</i> (preposición + -ing)",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the -ing form", instr="Escribe el gerundio.", items=[
   "read → [reading]", "dance → [dancing]", "swim → [swimming]", "cook → [cooking]", "ride → [riding]", "get up → [getting up]",
   "travel → [travelling]", "shop → [shopping]", "write → [writing]", "fish → [fishing]"]),
  dict(tipo="fill", titulo="Complete with the gerund", instr="Completa con el verbo en -ing.", items=[
   "I love [playing] (play) the guitar.", "She hates [doing] (do) homework.", "We enjoy [going] (go) to the beach.", "He doesn't mind [washing] (wash) the dishes.",
   "They can't stand [waiting] (wait).", "Do you like [watching] (watch) series?", "My dad enjoys [fishing] (fish).", "I'm good at [drawing] (draw).",
   "She is interested in [learning] (learn) Japanese.", "My cat loves [sleeping] (sleep) in the sun."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I enjoy {to dance|dancing*}.", "She {like|likes*} reading.", "Do you like {swimming*|swim}?", "He {doesn't mind*|don't mind} cooking.",
   "We are good at {play|playing*} football.", "They {hates|hate*} getting up early.", "{Does*|Do} your brother like sailing?", "I can't stand {to be|being*} late."]),
  dict(tipo="match", titulo="Match the symbols and the verbs", instr="Une el símbolo con la expresión.", pares=[
   ("(++)", "love"), ("(+)", "like / enjoy"), ("(0)", "don't mind"), ("(-)", "don't like"), ("(- -)", "hate / can't stand")]),
  dict(tipo="rewrite", titulo="Write sentences", instr="Escribe oraciones con la información.", cols=2, items=[
   "Sofía / (++) / dance => Sofía loves dancing.", "my dad / (- -) / shop => My dad hates shopping.", "I / (+) / read comics => I like reading comics.",
   "we / (0) / walk => We don't mind walking.", "Tom / (-) / swim => Tom doesn't like swimming.", "they / (+) / travel => They enjoy travelling."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con los verbos del recuadro en -ing.", banco=["sail", "listen", "cook", "get up", "clean", "play", "watch", "eat"], texto=
   "My name is Emilia. I love [sailing] — I go with my uncle every summer. I also enjoy [listening] to music and [playing] the bass guitar. "
   "I don't mind [cleaning] my room, but I hate [getting up] early on Saturdays. My brother likes [cooking]; he makes great pizzas, "
   "and I love [eating] them! In the evening, we enjoy [watching] films together."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "I enjoy to swim. => I enjoy swimming.", "She love dancing. => She loves dancing.", "Do you like play chess? => Do you like playing chess?",
   "He don't mind waiting. => He doesn't mind waiting.", "I'm good at sing. => I'm good at singing.", "They hates studying. => They hate studying."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My grandfather loves telling stories.", "Do you enjoy working in a team?", "I can't stand waiting for the bus.", "She is interested in studying marine biology."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Find a pen pal!", texto=
   "Hi! I'm Kai and I'm from New Zealand. I'm sixteen. I love surfing and I enjoy taking photos of the ocean. "
   "I don't mind doing homework, but I hate getting up early in winter. I'm good at cooking — my fish tacos are famous in my family! "
   "I'm interested in learning Spanish because I want to visit Chile. Do you like surfing? Write to me!",
   vf=[("Kai is from Australia.", False), ("He loves surfing.", True), ("He hates doing homework.", False), ("He wants to visit Chile.", True)],
   preguntas=["What is Kai good at? => He is good at cooking.", "Why is he interested in learning Spanish? => Because he wants to visit Chile."]),
  dict(tipo="write", titulo="Answer Kai's message", instr="Escribe tu respuesta a Kai usando gerundios.", items=[
   "Hi Kai! I'm … I love", "I enjoy", "I don't mind … but I hate", "I'm good at", "I'm interested in"]),
 ]),

# ------------------------------------------------------------------ PAST: WAS / WERE
dict(slug="past-was-were", titulo="Past Simple: Was / Were", nivel="2°", cefr="A2",
 objetivo="usar el pasado del verbo to be (was / were) en oraciones y preguntas.",
 goal="use was and were to talk about the past.",
 recordar=[
  "I / He / She / It → <b>was</b>  ·  You / We / They → <b>were</b>",
  "Negativo: <b>wasn't</b> / <b>weren't</b>  ·  Pregunta: <b>Was</b> she…? <b>Were</b> you…? → Yes, I was. / No, they weren't.",
  "Marcadores: <i>yesterday, last night, last week, two days ago, in 2010, when I was a child</i>",
  "<b>there was</b> (singular) / <b>there were</b> (plural) = había",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Complete with was or were", instr="Completa con was o were.", items=[
   "I [was] at home yesterday.", "They [were] in Santiago last week.", "She [was] very happy.", "We [were] late for class.",
   "The film [was] boring.", "You [were] my best friend in primary school.", "My parents [were] at work.", "It [was] cold last night.",
   "The ships [were] in the port.", "My grandfather [was] a sailor.", "There [was] a storm.", "There [were] many people at the party."]),
  dict(tipo="fill", titulo="Make it negative", instr="Completa con wasn't o weren't.", items=[
   "I [wasn't] tired.", "They [weren't] at school.", "The test [wasn't] difficult.", "We [weren't] hungry.", "He [wasn't] at the party.", "The shops [weren't] open."]),
  dict(tipo="rewrite", titulo="Write questions and short answers", instr="Escribe la pregunta y responde.", cols=2, items=[
   "you / at home (Yes) => Were you at home? Yes, I was.", "she / sick (No) => Was she sick? No, she wasn't.", "they / at the beach (Yes) => Were they at the beach? Yes, they were.",
   "the film / good (No) => Was the film good? No, it wasn't.", "he / in the lab (Yes) => Was he in the lab? Yes, he was.", "the cadets / tired (No) => Were the cadets tired? No, they weren't."]),
  dict(tipo="rewrite", titulo="Present to past", instr="Cambia la oración al pasado.", cols=2, items=[
   "I am tired. => I was tired.", "They are at home. => They were at home.", "She isn't here. => She wasn't here.",
   "Are you OK? => Were you OK?", "There is a problem. => There was a problem.", "There are two ships. => There were two ships."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "Where {was|were*} you last night?", "{Was*|Were} it expensive?", "My friends {wasn't|weren't*} at the match.", "I {was*|were} born in 2010.",
   "There {was|were*} three boats.", "{Was*|Were} the teacher angry?", "It {wasn't*|weren't} my fault.", "We {was|were*} in 1° Medio last year."]),
  dict(tipo="text", titulo="Complete the story", instr="Completa con was, were, wasn't o weren't.", texto=
   "Last Saturday [was] a great day. My friends and I [were] at the Naval Museum in Valparaíso. The museum [was] very interesting. "
   "There [were] old maps and models of ships. The guide [was] a retired officer and his stories [were] fantastic. "
   "The tickets [weren't] expensive — they [were] only 1,000 pesos. The only problem [was] the weather: it [was] very windy!"),
  dict(tipo="match", titulo="Match questions and answers", instr="Une pregunta y respuesta.", pares=[
   ("Where were you yesterday?", "I was at my grandma's house."), ("Was the test easy?", "No, it wasn't. It was hard."), ("Who was with you?", "My cousin Matías."),
   ("Were your parents angry?", "Yes, they were."), ("What was the weather like?", "It was sunny and warm."), ("How was the trip?", "It was amazing!")]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "Where were you last weekend?", "The museum was closed on Monday.", "There were many tourists in the port.", "Was your father a fisherman?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="When my grandmother was young", texto=
   "My grandmother Elena was born in 1958 in Talcahuano. Her father was a sailor and her mother was a seamstress. They weren't rich, but they were happy. "
   "There were seven children in the family! Their house was small and it was near the sea. Elena's favourite place was the beach. "
   "She was a very good student and her favourite subject was History.",
   vf=[("Elena was born in Talcahuano.", True), ("Her mother was a sailor.", False), ("The family was rich.", False), ("There were seven children.", True)],
   preguntas=["Where was the house? => It was near the sea.", "What was her favourite subject? => History."]),
  dict(tipo="write", titulo="When I was a child", instr="Escribe sobre tu infancia.", items=[
   "When I was a child, I was", "My best friend was", "My favourite toy was", "My first school was"]),
 ]),

# ------------------------------------------------------------------ PAST REGULAR
dict(slug="past-regular", titulo="Past Simple: Regular Verbs", nivel="2°", cefr="A2",
 objetivo="formar y usar el pasado simple de verbos regulares (-ed) en oraciones afirmativas.",
 goal="use regular verbs in the past simple.",
 recordar=[
  "Regla general: <b>+ed</b> → work<b>ed</b>, play<b>ed</b> · terminados en -e: <b>+d</b> → live<b>d</b>, danc<b>ed</b>",
  "Consonante + y → <b>-ied</b>: study → stud<b>ied</b> (pero vocal + y: play → played) · CVC: stop → sto<b>pped</b>, plan → pla<b>nned</b>",
  "Pronunciación: /t/ worked, washed · /d/ played, cleaned · /id/ wanted, needed",
  "La forma es igual para todas las personas: <i>I / she / they worked.</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the past form", instr="Escribe el pasado del verbo.", items=[
   "work → [worked]", "live → [lived]", "study → [studied]", "stop → [stopped]", "play → [played]", "dance → [danced]",
   "cry → [cried]", "plan → [planned]", "visit → [visited]", "arrive → [arrived]", "carry → [carried]", "travel → [travelled]",
   "clean → [cleaned]", "want → [wanted]", "stay → [stayed]", "drop → [dropped]"]),
  dict(tipo="classify", titulo="Classify by spelling rule", instr="Escribe el pasado en la columna correcta.", categorias={
   "+ ED": ["watched", "opened", "enjoyed"], "+ D": ["smiled", "closed", "used"], "-IED": ["tried", "married", "worried"], "DOUBLE + ED": ["shopped", "chatted", "jogged"]}),
  dict(tipo="fill", titulo="Complete the sentences", instr="Escribe el verbo en pasado.", items=[
   "I [watched] (watch) a film last night.", "She [studied] (study) for the test.", "We [visited] (visit) the port yesterday.", "They [played] (play) football.",
   "He [stopped] (stop) the car.", "The ship [arrived] (arrive) at 6 a.m.", "My mum [cooked] (cook) fish.", "I [cleaned] (clean) my room.",
   "The baby [cried] (cry) all night.", "We [walked] (walk) to the beach."]),
  dict(tipo="classify", titulo="Pronunciation of -ed", instr="Clasifica según el sonido final.", categorias={
   "/t/": ["helped", "looked", "danced"], "/d/": ["played", "listened", "lived"], "/id/": ["wanted", "visited", "needed"]}),
  dict(tipo="text", titulo="Complete the diary", instr="Escribe los verbos en pasado.", texto=
   "Dear diary, yesterday [was] (be) a fantastic day. In the morning, I [helped] (help) my father on his boat. We [cleaned] (clean) the deck and [repaired] (repair) a net. "
   "At lunchtime we [cooked] (cook) fish on the beach. In the afternoon I [walked] (walk) to Cerro Concepción with my friends. "
   "We [talked] (talk) and [laughed] (laugh) a lot. At night I [watched] (watch) a documentary about whales and I [learned] (learn) many things."),
  dict(tipo="rewrite", titulo="Present to past", instr="Cambia la oración al pasado y agrega la expresión de tiempo.", cols=1, items=[
   "I play tennis. (yesterday) => I played tennis yesterday.", "She studies English. (last night) => She studied English last night.",
   "They travel to Peru. (last summer) => They travelled to Peru last summer.", "We stay at home. (on Sunday) => We stayed at home on Sunday.",
   "The ship stops in Arica. (two days ago) => The ship stopped in Arica two days ago."]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "I studyed a lot. => I studied a lot.", "She plaied the piano. => She played the piano.", "We stoped the bus. => We stopped the bus.",
   "They danceed. => They danced.", "He watch TV yesterday. => He watched TV yesterday.", "I arriveed late. => I arrived late."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "We visited the Naval Museum last week.", "My sister studied all night.", "The ferry arrived two hours late.", "I helped my grandmother yesterday."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A famous rescue", texto=
   "In 1916, the Chilean tug boat Yelcho sailed to Antarctica. Its captain, Luis Pardo, wanted to rescue 22 men from the British Endurance expedition. "
   "The men waited on Elephant Island for more than four months. The Yelcho arrived on 30th August and the crew rescued all the men. "
   "The world celebrated Captain Pardo as a hero.",
   vf=[("The Yelcho sailed to Antarctica.", True), ("The captain was Arturo Prat.", False), ("The men waited for two weeks.", False), ("The crew rescued all the men.", True)],
   preguntas=["How many men did Pardo want to rescue? => 22 men.", "When did the Yelcho arrive? => On 30th August (1916)."]),
  dict(tipo="write", titulo="What did you do last weekend?", instr="Escribe 4 oraciones con verbos regulares en pasado.", items=[
   "On Saturday I", "Then I", "On Sunday my family and I", "In the evening I"]),
 ]),
]
