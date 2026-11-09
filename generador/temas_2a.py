# 2° Medio (A2) — Gramática, parte A
TEMAS = [
# ------------------------------------------------------------------ PRESENT CONTINUOUS
dict(slug="present-continuous", titulo="Present Continuous", nivel="2°", cefr="A2",
 objetivo="describir acciones que ocurren en este momento con am / is / are + verbo-ing.",
 goal="describe actions happening now.",
 recordar=[
  "<b>Afirmativo:</b> I <b>am</b> work<b>ing</b> · He / She / It <b>is</b> work<b>ing</b> · You / We / They <b>are</b> work<b>ing</b>",
  "<b>Negativo:</b> I'm not / isn't / aren't + -ing  ·  <b>Pregunta:</b> Are you working? → Yes, I am. / No, I'm not.",
  "Ortografía: make → mak<b>ing</b> (se elimina -e) · swim → swi<b>mm</b>ing, run → ru<b>nn</b>ing (CVC dobla) · lie → l<b>ying</b>",
  "Marcadores: <i>now, right now, at the moment, today, Look! Listen!</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the -ing form", instr="Escribe el verbo con -ing (cuidado con la ortografía).", items=[
   "work → [working]", "make → [making]", "swim → [swimming]", "run → [running]", "write → [writing]", "sit → [sitting]",
   "play → [playing]", "dance → [dancing]", "lie → [lying]", "study → [studying]", "stop → [stopping]", "come → [coming]"]),
  dict(tipo="fill", titulo="Complete with the present continuous", instr="Usa am / is / are + -ing.", largo=True, items=[
   "I [am reading] (read) a book now.", "She [is cooking] (cook) dinner.", "They [are playing] (play) football.", "The ship [is leaving] (leave) the port.",
   "We [are studying] (study) English.", "He [is sleeping] (sleep) right now.", "You [are talking] (talk) too loud!", "It [is raining] (rain) at the moment.",
   "My parents [are watching] (watch) TV.", "The students [are swimming] (swim) in the pool."]),
  dict(tipo="rewrite", titulo="Make negative sentences", instr="Escribe en negativo.", cols=2, items=[
   "I'm sleeping. => I'm not sleeping.", "She is working. => She isn't working.", "They are running. => They aren't running.",
   "We are listening. => We aren't listening.", "He is driving. => He isn't driving.", "It is snowing. => It isn't snowing."]),
  dict(tipo="rewrite", titulo="Write questions and short answers", instr="Escribe la pregunta y responde.", cols=2, items=[
   "you / study (Yes) => Are you studying? Yes, I am.", "she / dance (No) => Is she dancing? No, she isn't.", "they / eat (Yes) => Are they eating? Yes, they are.",
   "he / work (No) => Is he working? No, he isn't.", "the crew / sleep (Yes) => Is the crew sleeping? Yes, it is.", "we / win (No) => Are we winning? No, we aren't."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "Look! The boat {is sinking*|are sinking}.", "I {am*|is} writing a message.", "They {isn't|aren't*} listening.", "{Is*|Are} your sister sleeping?",
   "What {are*|is} you doing?", "He is {siting|sitting*} next to me.", "We are {makeing|making*} a cake.", "Listen! Somebody {sings|is singing*}."]),
  dict(tipo="text", titulo="Complete the text", instr="Usa el presente continuo de los verbos entre paréntesis.", texto=
   "It's Saturday morning at the port. The sun [is shining] (shine) and some tourists [are taking] (take) photos. "
   "A big cruise ship [is arriving] (arrive). Two fishermen [are selling] (sell) fish near the pier. A boy [is eating] (eat) an ice cream "
   "and his dog [is running] (run) after the seagulls. I [am sitting] (sit) on a bench and I [am writing] (write) this text. "
   "My friends [aren't working] (not work) today."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "She cooking now. => She is cooking now.", "They is playing. => They are playing.", "I'm runing. => I'm running.",
   "He are swimming. => He is swimming.", "Are she reading? => Is she reading?", "We aren't sleep. => We aren't sleeping."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My brother is playing video games.", "What are you doing right now?", "The students aren't listening to the teacher.", "Is it raining in Valparaíso?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el mensaje y responde.", titulo_texto="Message from the ship", texto=
   "Hi Mum! I'm writing from the training ship. We are sailing to Coquimbo now. The sea is calm and the sun is shining. "
   "At the moment, some cadets are cleaning the deck and others are studying navigation with the officer. My friend Tomás is cooking with the chef. "
   "I'm not feeling seasick today! I miss you. Love, Clara.",
   vf=[("Clara is writing from home.", False), ("They are sailing to Coquimbo.", True), ("Tomás is cleaning the deck.", False), ("Clara is feeling seasick.", False)],
   preguntas=["What are some cadets studying? => They are studying navigation.", "What is the weather like? => The sea is calm and the sun is shining."]),
  dict(tipo="write", titulo="What are they doing now?", instr="Imagina qué están haciendo estas personas ahora mismo.", items=[
   "My mother", "My best friend", "My classmates", "I"]),
 ]),

# ------------------------------------------------------------------ PRESENT SIMPLE vs CONTINUOUS
dict(slug="present-simple-vs-continuous", titulo="Present Simple vs Continuous", nivel="2°", cefr="A2",
 objetivo="distinguir entre hábitos (presente simple) y acciones en progreso (presente continuo).",
 goal="choose between the present simple and the present continuous.",
 recordar=[
  "<b>Present simple</b> → hábitos, rutinas, hechos: <i>I <b>work</b> every day.</i>  Marcadores: always, usually, every day, on Mondays",
  "<b>Present continuous</b> → ahora / temporal: <i>I <b>am working</b> now.</i>  Marcadores: now, at the moment, today, this week, Look!",
  "Verbos de estado no usan -ing: <b>like, love, hate, want, know, need, understand, believe</b> → <i>I want</i> (no: <i>I'm wanting</i>)",
 ],
 ejercicios=[
  dict(tipo="classify", titulo="Classify the time expressions", instr="Clasifica las expresiones.", categorias={
   "PRESENT SIMPLE": ["every day", "usually", "on Sundays", "never", "twice a week"], "PRESENT CONTINUOUS": ["now", "at the moment", "right now", "this week", "Look!"]}),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la forma correcta.", items=[
   "I {play*|am playing} football every Saturday.", "Look! The dog {swims|is swimming*}.", "She {works*|is working} in a bank.", "Shh! The baby {sleeps|is sleeping*}.",
   "We usually {go*|are going} to school by bus.", "Today we {walk|are walking*} because the bus is broken.", "I {know*|am knowing} the answer.",
   "He {doesn't like*|isn't liking} fish.", "What {do you do|are you doing*} now?", "The sun {rises*|is rising} in the east."]),
  dict(tipo="fill", titulo="Complete the sentences", instr="Usa presente simple o continuo.", largo=True, items=[
   "My dad usually [drives] (drive) to work.", "Today he [is taking] (take) the bus.", "I [don't understand] (not understand) this word.",
   "Listen! Someone [is playing] (play) the guitar.", "She [visits] (visit) her grandma every Sunday.", "Right now, they [are having] (have) lunch.",
   "We [need] (need) more time.", "It often [rains] (rain) in winter.", "Be quiet! I [am studying] (study).", "The ship [leaves] (leave) every day at six."]),
  dict(tipo="text", titulo="Complete the text", instr="Usa la forma correcta de los verbos.", texto=
   "Rodrigo is a fisherman. He usually [gets] (get) up at four o'clock and [goes] (go) to sea with his brother. They normally [catch] (catch) hake and conger eel. "
   "But today is different. Today Rodrigo [is staying] (stay) at home because there is a storm. At the moment he [is repairing] (repair) his nets "
   "and his wife [is making] (make) bread. Rodrigo [loves] (love) his job, but he [doesn't like] (not like) storms!"),
  dict(tipo="rewrite", titulo="Write two sentences", instr="Escribe una oración en presente simple y otra en continuo.", cols=1, items=[
   "Ana / play tennis (every Friday / now: swim) => Ana plays tennis every Friday. Now she is swimming.",
   "my parents / work in Santiago (usually / this week: work in Valparaíso) => My parents usually work in Santiago. This week they are working in Valparaíso.",
   "I / wear a uniform (on weekdays / today: wear jeans) => I wear a uniform on weekdays. Today I am wearing jeans."]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "I am wanting a pizza. => I want a pizza.", "She is going to school every day. => She goes to school every day.", "Look! It rains. => Look! It's raining.",
   "He doesn't playing now. => He isn't playing now.", "Do you understanding? => Do you understand?", "They are usually eat at 2. => They usually eat at 2."]),
  dict(tipo="match", titulo="Match questions and answers", instr="Une pregunta y respuesta.", pares=[
   ("What do you do?", "I'm a student."), ("What are you doing?", "I'm doing my homework."), ("Do you like the sea?", "Yes, I love it."),
   ("Are you listening?", "Sorry, no. What did you say?"), ("Where does she work?", "In a hotel."), ("Where is she going?", "To the bank.")]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "I usually walk to school.", "Today I am taking the bus.", "What is your mother doing now?", "He doesn't work on Sundays."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A week on Rapa Nui", texto=
   "Normally, Daniela lives in Valparaíso and studies tourism. She takes the bus every day and works in a café on weekends. "
   "But this week she is visiting Rapa Nui with her class. They are staying in a small hotel near the beach. Every morning they visit a different moai. "
   "Right now, Daniela is swimming in Anakena beach and her friends are taking photos. She loves this island!",
   vf=[("Daniela studies tourism.", True), ("She is working in a café this week.", False), ("They are staying in a hotel near the beach.", True), ("She is swimming right now.", True)],
   preguntas=["What does she do on weekends? => She works in a café.", "What are her friends doing now? => They are taking photos."]),
  dict(tipo="write", titulo="Your turn", instr="Escribe 2 oraciones sobre tus hábitos y 2 sobre lo que pasa ahora en la sala.", items=[
   "Every day I", "On weekends I", "Right now I", "At the moment my classmates"]),
 ]),

# ------------------------------------------------------------------ CAN
dict(slug="can", titulo="Modal Verb: Can", nivel="2°", cefr="A2",
 objetivo="expresar habilidad, posibilidad y permiso con can / can't.",
 goal="talk about ability, possibility and permission with can.",
 recordar=[
  "<b>can</b> + verbo base (igual para todas las personas): <i>I can swim. She can swim.</i> (no: <i>She cans swims</i>)",
  "Negativo: <b>can't</b> (cannot) → <i>He can't drive.</i>  ·  Pregunta: <b>Can</b> you…? → Yes, I can. / No, I can't.",
  "Usos: habilidad (<i>I can speak English</i>), permiso (<i>Can I go out?</i>), pedido (<i>Can you help me?</i>), posibilidad (<i>You can see the sea from here</i>).",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Complete with can or can't", instr="Completa con can o can't según el sentido.", items=[
   "Fish [can] swim, but they [can't] walk.", "Birds [can] fly.", "A baby [can't] drive a car.", "Penguins [can't] fly, but they [can] swim.",
   "I [can't] see; it's too dark.", "Dogs [can't] speak.", "A good sailor [can] tie knots.", "You [can't] smoke on the ship. It's prohibited."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "She can {swim*|swims|to swim} very well.", "{Can I*|I can} open the window?", "He {can't*|doesn't can} cook.", "{Can you*|Do you can} help me?",
   "They can {plays|play*} the guitar.", "Yes, I {can*|do}.", "My grandma {cans|can*} speak Italian.", "We {can't*|not can} go out today."]),
  dict(tipo="rewrite", titulo="Make questions and answer", instr="Escribe la pregunta y responde.", cols=2, items=[
   "you / swim (Yes) => Can you swim? Yes, I can.", "she / drive (No) => Can she drive? No, she can't.", "they / speak English (Yes) => Can they speak English? Yes, they can.",
   "he / cook (No) => Can he cook? No, he can't.", "I / use your pen (Yes) => Can I use your pen? Yes, you can.", "your dog / jump (Yes) => Can your dog jump? Yes, it can."]),
  dict(tipo="match", titulo="Ability, permission or request?", instr="Une cada oración con su función.", pares=[
   ("I can play the piano.", "ability"), ("Can I go to the toilet?", "permission"), ("Can you close the door, please?", "request"),
   ("You can see the port from my house.", "possibility"), ("He can't swim.", "lack of ability")]),
  dict(tipo="text", titulo="Complete the job advertisement", instr="Completa con can, can't o Can.", texto=
   "JOB OFFER: Assistant on a tourist boat. [Can] you speak English? [Can] you work on weekends? Then this job is for you! "
   "You [can] start next month. The ideal person [can] swim and [can] help tourists. People who [can't] work in the sun all day "
   "should not apply. You [can] send your CV to jobs@bahia.cl."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "She can swims. => She can swim.", "I can to drive. => I can drive.", "Do you can help me? => Can you help me?",
   "He cans play chess. => He can play chess.", "They don't can come. => They can't come.", "Can she sings? => Can she sing?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My father can repair engines.", "Can you speak French?", "I can't find my keys.", "Can I borrow your phone, please?", "Sailors can tie many knots."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Superpowers of the sea", texto=
   "Sea animals have amazing abilities. Dolphins can swim at 40 km per hour and they can communicate with sounds. Octopuses can change colour and they can open jars. "
   "Sea turtles can live for more than 100 years, but they can't breathe underwater; they need to go to the surface. "
   "Some fish can fly for a few seconds over the water!",
   vf=[("Dolphins can swim at 40 km/h.", True), ("Octopuses can change colour.", True), ("Turtles can breathe underwater.", False), ("No fish can fly.", False)],
   preguntas=["What can octopuses open? => They can open jars.", "How long can sea turtles live? => More than 100 years."]),
  dict(tipo="write", titulo="About you", instr="Escribe sobre tus habilidades.", items=[
   "I can … very well.", "I can't", "My best friend can", "I want to learn to … because"]),
 ]),

# ------------------------------------------------------------------ ADVERBS OF FREQUENCY
dict(slug="adverbs-frequency", titulo="Adverbs of Frequency", nivel="2°", cefr="A2",
 objetivo="expresar con qué frecuencia hacemos las cosas y ubicar correctamente los adverbios.",
 goal="say how often you do things using adverbs of frequency.",
 recordar=[
  "<b>always</b> 100% · <b>usually</b> 80% · <b>often</b> 60% · <b>sometimes</b> 40% · <b>rarely / hardly ever</b> 10% · <b>never</b> 0%",
  "Posición: <b>antes del verbo principal</b> → <i>I <b>often</b> play football.</i> · <b>después de to be</b> → <i>She is <b>always</b> late.</i>",
  "Preguntar: <i><b>How often</b> do you…?</i> → <i>once a week, twice a month, three times a year, every day</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Order the adverbs", instr="Escribe el adverbio según el porcentaje.", items=[
   "100% → [always]", "80% → [usually]", "60% → [often]", "40% → [sometimes]", "10% → [rarely / hardly ever]", "0% → [never]"]),
  dict(tipo="rewrite", titulo="Put the adverb in the correct place", instr="Reescribe la oración con el adverbio.", cols=2, items=[
   "I eat breakfast. (always) => I always eat breakfast.", "She is late. (never) => She is never late.", "We go to the cinema. (sometimes) => We sometimes go to the cinema.",
   "He plays tennis. (often) => He often plays tennis.", "They are tired. (usually) => They are usually tired.", "My dad cooks. (rarely) => My dad rarely cooks.",
   "The ferry is on time. (always) => The ferry is always on time.", "I drink coffee. (never) => I never drink coffee."]),
  dict(tipo="choice", titulo="Choose the correct sentence", instr="Encierra la oración correcta.", cols=1, items=[
   "{I always am happy.|I am always happy.*}", "{She often visits her grandma.*|She visits often her grandma.}", "{We never are late.|We are never late.*}",
   "{Do you usually walk to school?*|Do usually you walk to school?}", "{He sometimes is angry.|He is sometimes angry.*}", "{They hardly ever eat fish.*|They eat hardly ever fish.}"]),
  dict(tipo="fill", titulo="How often?", instr="Escribe la expresión de frecuencia.", items=[
   "1 time per week → [once a week]", "2 times per month → [twice a month]", "3 times per year → [three times a year]", "Monday to Sunday → [every day]",
   "on Saturdays and Sundays → [every weekend]", "1 time per day → [once a day]"]),
  dict(tipo="text", titulo="Complete the text", instr="Elige el adverbio lógico del recuadro.", banco=["always", "usually", "often", "sometimes", "never", "hardly ever"], texto=
   "My brother Pablo is very organised. He [always] gets up at 6:00, every single day. He [usually] has breakfast at home, but sometimes he eats at school. "
   "He [often] goes to the gym — about four times a week. He [sometimes] plays video games, maybe twice a month. "
   "He [hardly ever] watches TV, only during the World Cup. And he [never] eats junk food — not even once!"),
  dict(tipo="rewrite", titulo="Answer the questions about you", instr="Responde con un adverbio de frecuencia.", cols=1, items=[
   "How often do you eat fish? => I … eat fish.", "How often are you late for school? => I am … late for school.",
   "How often do you go to the beach? => I … go to the beach.", "How often do you help at home? => I … help at home."]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige la posición del adverbio.", cols=2, items=[
   "I go always to bed at 10. => I always go to bed at 10.", "She never is sad. => She is never sad.", "Usually we eat at 2. => We usually eat at 2.",
   "He plays sometimes the drums. => He sometimes plays the drums."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My mother always drinks tea in the morning.", "How often do you visit your grandparents?", "We are never bored in English class.", "They sometimes go fishing on Sundays."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Life on a cargo ship", texto=
   "Life on a cargo ship is very regular. The crew always eats at the same time: breakfast at seven, lunch at twelve and dinner at six. "
   "They usually work eight hours a day. They sometimes have free time to watch films or play cards. "
   "The sailors hardly ever see their families — maybe twice a year. They often feel tired, but they are never bored because the sea is always changing.",
   vf=[("The crew eats at different times every day.", False), ("They usually work eight hours.", True), ("They often see their families.", False), ("They are never bored.", True)],
   preguntas=["How often do the sailors see their families? => Maybe twice a year.", "What do they sometimes do in their free time? => They watch films or play cards."]),
  dict(tipo="write", titulo="Your habits", instr="Escribe una oración con cada adverbio.", items=["always", "usually", "sometimes", "never"]),
 ]),
]
