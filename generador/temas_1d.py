# 1° Medio (A1) — Gramática, parte D
TEMAS = [
# ------------------------------------------------------------------ POSSESSIVE 'S
dict(slug="possessive-s", titulo="Possessive 's", nivel="1°", cefr="A1",
 objetivo="usar el genitivo sajón ('s / s') para indicar de quién es algo.",
 goal="use 's and s' to show possession.",
 recordar=[
  "Persona singular + <b>'s</b>: <i>Ana<b>'s</b> bag</i> (la mochila de Ana) · <i>the captain<b>'s</b> ship</i>",
  "Plural terminado en s + <b>'</b>: <i>my parents<b>'</b> car</i> · plurales irregulares + <b>'s</b>: <i>the children<b>'s</b> toys</i>",
  "<b>Whose</b> …? = ¿De quién…? → <i>Whose phone is this? It's Pedro's.</i>  ·  Cuidado: <i>Ana's</i> también puede ser <i>Ana is</i>.",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the possessive form", instr="Escribe la forma posesiva.", items=[
   "the bag of Sofía → [Sofía's] bag", "the car of my father → my [father's] car", "the toys of the children → the [children's] toys",
   "the house of my parents → my [parents'] house", "the dog of Tom → [Tom's] dog", "the ship of the captain → the [captain's] ship",
   "the room of the girls → the [girls'] room", "the phone of my sister → my [sister's] phone"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "This is {Maria's*|Marias'} pencil.", "My {brothers's|brothers'*} bedroom is big. (2 brothers)", "The {women's*|womens'} team won.",
   "{Whose*|Who's} bag is this?", "It's my {teacher's*|teachers} book.", "The {students'*|student's} uniforms are blue. (all students)",
   "My {mom's*|mom} name is Paula.", "The {dog's*|dogs'} bone is under the table. (1 dog)"]),
  dict(tipo="rewrite", titulo="Rewrite with 's or s'", instr="Reescribe usando el genitivo sajón.", cols=2, items=[
   "The name of my dog is Max. => My dog's name is Max.", "The bikes of the boys are new. => The boys' bikes are new.",
   "The office of the director is here. => The director's office is here.", "The shoes of Carla are red. => Carla's shoes are red.",
   "The games of the children are fun. => The children's games are fun.", "The house of my grandparents is old. => My grandparents' house is old."]),
  dict(tipo="text", titulo="Complete the family text", instr="Completa con la forma posesiva del nombre entre paréntesis.", texto=
   "This is my family. My [father's] (father) name is Raúl. My [mother's] (mother) name is Gloria. My [grandparents'] (grandparents) house is in Quilpué. "
   "My [brother's] (brother) girlfriend is called Daniela. My [cousins'] (cousins, plural) favourite place is the beach. "
   "And our [dog's] (dog) name is Pirata!"),
  dict(tipo="match", titulo="Whose is it?", instr="Une cada objeto con su dueño lógico.", pares=[
   ("the stethoscope", "It's the doctor's."), ("the anchor", "It's the sailor's."), ("the whistle", "It's the referee's."),
   ("the toys", "They're the children's."), ("the chalk", "It's the teacher's."), ("the bone", "It's the dog's.")]),
  dict(tipo="fill", titulo="IS or POSSESSIVE?", instr="Escribe IS si 's significa 'is' o P si es posesivo.", items=[
   "Ana's tired. → [IS]", "Ana's bag is red. → [P]", "My brother's car is new. → [P]", "My brother's at home. → [IS]",
   "Tom's a sailor. → [IS]", "Tom's ship is big. → [P]"]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "This is the bag of Ana. => This is Ana's bag.", "My parent's car is old. (2 parents) => My parents' car is old.", "The childrens' toys are here. => The children's toys are here.",
   "Who's phone is this? => Whose phone is this?", "Pedros book is blue. => Pedro's book is blue.", "The mans' hat is black. => The man's hat is black."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My uncle's boat is in the port.", "Whose jacket is this?", "The students' lab is on the second floor.", "Is this your sister's phone?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Lost and found", texto=
   "At the end of the day, our teacher found many things in the classroom. There was a blue pencil case — it was Benjamín's. "
   "There was a red jacket — it was Isidora's. There were two water bottles — they were the twins' bottles. "
   "There was also a phone, but nobody knew whose phone it was. In the end, it was the teacher's phone!",
   vf=[("The blue pencil case was Isidora's.", False), ("The red jacket was Isidora's.", True), ("The water bottles were the twins'.", True), ("The phone was Benjamín's.", False)],
   preguntas=["Whose phone was it? => It was the teacher's phone.", "Whose pencil case was it? => It was Benjamín's."]),
  dict(tipo="write", titulo="Your turn", instr="Escribe sobre tu familia o amigos usando 's.", items=[
   "My mother's", "My best friend's", "My grandparents'"]),
 ]),

# ------------------------------------------------------------------ PREPOSITIONS OF PLACE
dict(slug="prepositions-place", titulo="Prepositions of Place", nivel="1°", cefr="A1",
 objetivo="describir la ubicación de objetos y personas con preposiciones de lugar.",
 goal="say where things are using prepositions of place.",
 recordar=[
  "<b>in</b> (dentro) · <b>on</b> (sobre, en contacto) · <b>under</b> (debajo) · <b>behind</b> (detrás) · <b>in front of</b> (delante)",
  "<b>next to</b> (al lado) · <b>between</b> (entre dos) · <b>opposite</b> (frente a) · <b>above</b> (encima, sin contacto) · <b>near</b> (cerca)",
  "Ejemplo: <i>The ship is <b>between</b> the ferry and the boat. The lighthouse is <b>near</b> the port.</i>",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the preposition and the meaning", instr="Une la preposición con su significado.", pares=[
   ("in", "dentro de"), ("on", "sobre (tocando)"), ("under", "debajo de"), ("behind", "detrás de"), ("in front of", "delante de"),
   ("next to", "al lado de"), ("between", "entre"), ("opposite", "frente a")]),
  dict(tipo="fill", titulo="Complete with a preposition", instr="Usa las preposiciones del recuadro.", banco=["in", "on", "under", "behind", "next to", "between", "in front of", "above"], items=[
   "The books are [on] the desk.", "The cat is sleeping [under] the bed.", "My phone is [in] my bag.", "The clock is [above] the board.",
   "The teacher stands [in front of] the class.", "Pedro sits [between] Ana and Luis.", "The bathroom is [next to] the kitchen.", "The car is [behind] the house."]),
  dict(tipo="choice", titulo="Choose the correct preposition", instr="Encierra la opción correcta.", items=[
   "The fish are {in*|on} the water.", "The picture is {on*|in} the wall.", "The ball is {under*|on} the table (on the floor).",
   "The bank is {opposite*|between} the school, across the street.", "Valparaíso is {next to|near*} Viña del Mar.", "The keys are {in*|on} the drawer.",
   "The lamp is {above*|under} the table.", "The ship is {between*|next} two boats."]),
  dict(tipo="text", titulo="Complete the description of a classroom", instr="Completa con in, on, under, next to, between, behind, in front of.", texto=
   "In my classroom, the teacher's desk is [in front of] the board. There is a computer [on] the desk. My bag is [under] my chair. "
   "I sit [next to] the window. My friend Nicolás sits [between] me and Josefa. The lockers are [behind] the students, at the back of the room. "
   "There are many posters [on] the walls and some books [in] the cupboard."),
  dict(tipo="rewrite", titulo="Answer the questions", instr="Responde con la preposición indicada.", cols=2, items=[
   "Where is the dog? (under / table) => It's under the table.", "Where are the keys? (in / my pocket) => They're in my pocket.",
   "Where is the ship? (next to / ferry) => It's next to the ferry.", "Where is Ana? (behind / Tomás) => She's behind Tomás.",
   "Where is the map? (on / wall) => It's on the wall.", "Where is the bank? (opposite / park) => It's opposite the park."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "The lighthouse is near the port.", "My shoes are under the bed.", "The pharmacy is between the bank and the café.", "Is your phone in your bag?"]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige la preposición incorrecta.", cols=2, items=[
   "The book is in the table. => The book is on the table.", "I sit next Ana. => I sit next to Ana.", "The cat is between the bed. => The cat is under the bed.",
   "The fish is on the water. => The fish is in the water.", "The bank is opposite of the park. => The bank is opposite the park.", "She is in front the door. => She is in front of the door."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="My street", texto=
   "I live on Avenida Brasil. My house is between a small café and a bookshop. Opposite my house there is a big park with trees. "
   "Next to the park there is a supermarket. The bus stop is in front of the supermarket. Behind my house, you can see the hills of Valparaíso. "
   "My favourite place is the café next to my house — it has the best cakes!",
   vf=[("The house is between a café and a bookshop.", True), ("The park is behind the house.", False), ("The bus stop is in front of the supermarket.", True), ("The supermarket is next to the park.", True)],
   preguntas=["What is opposite the house? => A big park with trees.", "What can you see behind the house? => The hills of Valparaíso."]),
  dict(tipo="write", titulo="Describe your bedroom", instr="Escribe 5 oraciones con preposiciones de lugar.", items=[
   "My bed is", "My bag is", "There is a … on", "My … is next to", "The window is"]),
 ]),

# ------------------------------------------------------------------ QUESTION WORDS
dict(slug="question-words", titulo="Question Words (Wh-)", nivel="1°", cefr="A1",
 objetivo="formular preguntas con what, where, when, who, why, how, how many, how old y whose.",
 goal="ask questions with question words.",
 recordar=[
  "<b>What</b> (qué) · <b>Where</b> (dónde) · <b>When</b> (cuándo) · <b>Who</b> (quién) · <b>Why</b> (por qué) → <i>Because…</i> · <b>Which</b> (cuál)",
  "<b>How</b> (cómo) · <b>How old</b> (edad) · <b>How many</b> (cuántos) · <b>How much</b> (cuánto / precio) · <b>What time</b> (a qué hora) · <b>Whose</b> (de quién)",
  "Orden: <b>Wh- + to be + sujeto</b> → <i>Where is the port?</i>  ·  <b>Wh- + do / does + sujeto + verbo</b> → <i>Where do you live?</i>",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the question word and the answer", instr="Une la palabra con el tipo de respuesta.", pares=[
   ("Where…?", "In Valparaíso."), ("When…?", "On Monday."), ("Who…?", "My sister."), ("Why…?", "Because I'm tired."), ("How old…?", "Fifteen."),
   ("How many…?", "Three."), ("What time…?", "At 8 o'clock."), ("How much…?", "2,000 pesos.")]),
  dict(tipo="fill", titulo="Complete with a question word", instr="Completa con la palabra interrogativa correcta.", items=[
   "[Where] do you live? — In Playa Ancha.", "[How old] are you? — I'm sixteen.", "[What] is your name? — Martín.", "[When] is your birthday? — In May.",
   "[Who] is your teacher? — Mr. Ramírez.", "[Why] are you sad? — Because I lost my phone.", "[How many] brothers do you have? — Two.",
   "[What time] does class start? — At 8:00.", "[How much] is this cap? — 5,000 pesos.", "[Whose] bag is this? — It's Ana's.",
   "[How] are you? — I'm fine, thanks.", "[Which] colour do you prefer, red or blue? — Blue."]),
  dict(tipo="choice", titulo="Choose the correct question word", instr="Encierra la opción correcta.", items=[
   "{What|Where*} is the bus stop?", "{Who*|What} is that man?", "{How many*|How much} students are there?", "{How much*|How many} is the ticket?",
   "{When*|Where} does the ship arrive? — Tomorrow.", "{Why*|What} do you study here? — Because I like the sea.", "{How*|What} do you go to school? — By bus.",
   "{Whose*|Who's} shoes are these?"]),
  dict(tipo="rewrite", titulo="Write the question", instr="Escribe la pregunta para la respuesta (la parte en negrita).", cols=1, items=[
   "I live <b>in Viña del Mar</b>. => Where do you live?", "My name is <b>Catalina</b>. => What is your name?", "I'm <b>fifteen</b>. => How old are you?",
   "The class starts <b>at nine</b>. => What time does the class start?", "<b>My father</b> cooks dinner. => Who cooks dinner?",
   "I have <b>two</b> cats. => How many cats do you have?", "She is sad <b>because she is sick</b>. => Why is she sad?", "My birthday is <b>in October</b>. => When is your birthday?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras para formar preguntas.", items=[
   "Where does your mother work?", "What is your favourite food?", "How many students are in your class?", "When do you play football?", "Why are you late?"]),
  dict(tipo="text", titulo="Complete the interview", instr="Completa la entrevista con palabras interrogativas.", texto=
   "REPORTER: Hello! [What] is your name?\nSAILOR: My name is Carlos Fuentes.\nREPORTER: [How old] are you?\nSAILOR: I'm thirty-two.\n"
   "REPORTER: [Where] do you work?\nSAILOR: On a cargo ship called 'Andes'.\nREPORTER: [How many] people work on the ship?\nSAILOR: Twenty-five.\n"
   "REPORTER: [Why] do you like your job?\nSAILOR: Because I love the sea and travelling.\nREPORTER: [When] do you see your family?\nSAILOR: Every two months."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error en cada pregunta.", cols=2, items=[
   "Where you live? => Where do you live?", "What is you name? => What is your name?", "How many money do you have? => How much money do you have?",
   "Who old are you? => How old are you?", "Where does she works? => Where does she work?", "Why you are sad? => Why are you sad?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el perfil y responde las preguntas.", titulo_texto="Student profile", texto=
   "Name: Josefa Medina · Age: 16 · From: Quillota · School: Instituto Marítimo, 1° Medio\n"
   "Josefa lives with her mother and two brothers. She travels to Valparaíso by train every day. Her classes start at 8:00 and finish at 16:30. "
   "Her favourite subject is English because she wants to work on cruise ships. On weekends she plays volleyball with her friends.",
   preguntas=["Where is Josefa from? => She is from Quillota.", "How old is she? => She is sixteen.", "How does she travel to school? => By train.",
              "What time do her classes finish? => At 16:30.", "Why is English her favourite subject? => Because she wants to work on cruise ships.",
              "What does she do on weekends? => She plays volleyball with her friends."]),
  dict(tipo="write", titulo="Interview a classmate", instr="Escribe 5 preguntas, hazlas a un compañero y anota sus respuestas.", items=[
   "Where", "What", "When", "How many", "Why"]),
 ]),

# ------------------------------------------------------------------ IMPERATIVES
dict(slug="imperatives", titulo="Imperatives", nivel="1°", cefr="A1",
 objetivo="dar instrucciones, órdenes y advertencias usando el imperativo.",
 goal="give instructions and warnings with imperatives.",
 recordar=[
  "<b>Afirmativo:</b> verbo en forma base → <i>Open the door. Sit down. Listen!</i>",
  "<b>Negativo:</b> <b>Don't</b> + verbo → <i>Don't run. Don't touch the engine!</i>",
  "Más amable con <b>please</b>: <i>Close the window, please.</i>  ·  Para sugerir: <b>Let's</b> + verbo → <i>Let's go!</i>",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the instruction and the place", instr="Une cada instrucción con el lugar donde la ves.", pares=[
   ("Wear a life jacket.", "On a boat"), ("Don't use your phone.", "In an exam"), ("Be quiet.", "In a library"), ("Wash your hands.", "In a kitchen"),
   ("Don't swim here.", "At a dangerous beach"), ("Fasten your seatbelt.", "On a plane"), ("Wear safety glasses.", "In a workshop")]),
  dict(tipo="fill", titulo="Complete the classroom instructions", instr="Usa los verbos del recuadro.", banco=["open", "listen", "sit", "write", "don't talk", "raise", "close", "don't eat"], items=[
   "[Open] your books on page 20.", "[Listen] to the audio.", "[Sit] down, please.", "[Write] your name here.",
   "[Don't talk] during the test.", "[Raise] your hand to answer.", "[Close] the door, please.", "[Don't eat] in the lab."]),
  dict(tipo="rewrite", titulo="Make negative imperatives", instr="Escribe la instrucción en negativo.", cols=2, items=[
   "Run in the corridor. => Don't run in the corridor.", "Touch the cables. => Don't touch the cables.", "Open the window. => Don't open the window.",
   "Be late. => Don't be late.", "Use your phone. => Don't use your phone.", "Shout. => Don't shout."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la instrucción lógica.", items=[
   "It's cold. {Close*|Open} the window.", "The floor is wet. {Run|Don't run*}!", "You are tired. {Go*|Don't go} to bed.",
   "It's dangerous. {Touch|Don't touch*} it!", "The test is easy. {Don't worry*|Worry}.", "The baby is sleeping. {Be*|Don't be} quiet.",
   "{Let's*|Let} go to the beach!", "It's raining. {Take*|Don't take} an umbrella."]),
  dict(tipo="text", titulo="Complete the safety rules", instr="Completa las reglas de seguridad del taller con imperativos (afirmativos o negativos).", banco=["wear", "don't run", "turn off", "don't touch", "listen", "keep", "don't eat", "wash"], texto=
   "WORKSHOP SAFETY RULES\n1. [Wear] safety glasses and gloves.\n2. [Don't run] in the workshop.\n3. [Listen] to the teacher's instructions.\n"
   "4. [Don't touch] machines without permission.\n5. [Keep] your area clean.\n6. [Don't eat] or drink near the machines.\n"
   "7. [Turn off] the machines after use.\n8. [Wash] your hands at the end of the class."),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "Please close the door.", "Don't forget your homework.", "Turn left at the corner.", "Let's study together."]),
  dict(tipo="fill", titulo="Give directions", instr="Completa las indicaciones para llegar al museo.", banco=["go", "turn", "cross", "walk", "stop"], items=[
   "[Go] straight on.", "[Turn] right at the bank.", "[Cross] the street.", "[Walk] for two blocks.", "[Stop] at the museum. It's on your left."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el cartel y responde.", titulo_texto="Welcome on board! — Ferry rules", texto=
   "Welcome to the ferry 'Pacífico'. Please read these rules. Keep your ticket with you. Don't stand near the edge of the ship. "
   "Children: always stay with an adult. Don't throw rubbish into the sea; use the bins. In an emergency, listen to the crew and put on your life jacket. "
   "Enjoy the trip!",
   vf=[("You can stand near the edge.", False), ("Children must stay with an adult.", True), ("You can throw rubbish into the sea.", False), ("In an emergency, listen to the crew.", True)],
   preguntas=["What must you keep with you? => Your ticket.", "What do you put on in an emergency? => A life jacket."]),
  dict(tipo="write", titulo="Write rules", instr="Escribe 4 reglas para tu sala de clases (2 afirmativas y 2 negativas).", items=["Rule:", "Rule:", "Rule:", "Rule:"]),
 ]),
]
