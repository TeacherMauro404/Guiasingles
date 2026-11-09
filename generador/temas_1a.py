# 1° Medio (A1) — Gramática, parte A
TEMAS = [
# ------------------------------------------------------------------ VERB TO BE
dict(slug="verb-to-be", titulo="Verb To Be", nivel="1°", cefr="A1",
 objetivo="usar am / is / are en oraciones afirmativas, negativas e interrogativas.",
 goal="use am / is / are to describe people, places and things.",
 recordar=[
  "<b>Afirmativo:</b> I <b>am</b> · He / She / It <b>is</b> · You / We / They <b>are</b>   (I'm, she's, they're)",
  "<b>Negativo:</b> I <b>am not</b> · He <b>isn't</b> · They <b>aren't</b>",
  "<b>Pregunta:</b> <b>Am</b> I…? · <b>Is</b> she…? · <b>Are</b> you…?   → Yes, I am. / No, she isn't.",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Complete with am, is or are", instr="Completa con la forma correcta del verbo to be.", items=[
   "I [am] a student.", "She [is] my sister.", "They [are] from Chile.", "The ship [is] very big.",
   "We [are] in 1° Medio.", "You [are] my best friend.", "My father [is] a sailor.", "It [is] cold today.",
   "Pedro and Ana [are] classmates.", "The port [is] near my house.", "I [am] fifteen years old.", "The books [are] on the table."]),
  dict(tipo="fill", titulo="Write the contraction", instr="Escribe la forma contraída.", items=[
   "I am → [I'm]", "she is → [she's]", "they are → [they're]", "we are → [we're]",
   "he is → [he's]", "it is → [it's]", "you are → [you're]", "is not → [isn't]",
   "are not → [aren't]", "Tom is → [Tom's]"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "My mother {is*|are|am} a nurse.", "We {is|are*|am} at school.", "I {is|are|am*} tired.",
   "The students {is|are*|am} in the lab.", "Valparaíso {is*|are|am} a port city.", "You {isn't|aren't*|am not} late.",
   "The teacher {isn't*|aren't|am not} here.", "{Is|Are*|Am} they your friends?", "{Is*|Are|Am} your brother tall?",
   "My cats {isn't|aren't*} black."]),
  dict(tipo="rewrite", titulo="Make the sentences negative", instr="Transforma las oraciones a la forma negativa (usa contracciones).", cols=2, items=[
   "She is happy. => She isn't happy.", "I am hungry. => I'm not hungry.", "They are at home. => They aren't at home.",
   "The boat is new. => The boat isn't new.", "We are tired. => We aren't tired.", "He is from Peru. => He isn't from Peru.",
   "It is my bag. => It isn't my bag.", "You are late. => You aren't late."]),
  dict(tipo="rewrite", titulo="Make questions and answer", instr="Escribe la pregunta y responde con una respuesta corta.", cols=2, items=[
   "He is a cook. (Yes) => Is he a cook? Yes, he is.", "They are sisters. (No) => Are they sisters? No, they aren't.",
   "You are fifteen. (Yes) => Are you fifteen? Yes, I am.", "It is a cat. (No) => Is it a cat? No, it isn't.",
   "She is at the port. (Yes) => Is she at the port? Yes, she is.", "We are late. (No) => Are we late? No, we aren't."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa el texto con am, is, are, isn't o aren't.", texto=
   "Hello! My name [is] Martín and I [am] sixteen years old. I [am] a student at the Instituto Marítimo. "
   "My school [is] in Valparaíso. My friends Diego and Camila [are] in my class. Diego [is] tall and funny. "
   "Camila [is] very intelligent. Our classroom [isn't] big, but it [is] nice. My teachers [are] friendly. "
   "We [aren't] tired today because it [is] Friday!"),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras para formar oraciones.", items=[
   "My brother is a mechanic.", "Are you from Valparaíso?", "We aren't in the classroom.",
   "The sea is blue today.", "Is your teacher Chilean?", "I am not very tall."]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Cada oración tiene un error. Reescríbela correctamente.", cols=2, items=[
   "She are my friend. => She is my friend.", "I is a student. => I am a student.", "They is at school. => They are at school.",
   "We am happy. => We are happy.", "He not is tall. => He isn't tall.", "Is they Chilean? => Are they Chilean?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el texto y responde.", titulo_texto="My new classmate", texto=
   "This is Valentina. She is fifteen years old and she is from Antofagasta. She is in 1° Medio at our school. "
   "Valentina is short and she has long dark hair. She is very friendly and good at English. Her parents are doctors. "
   "They are not from Valparaíso, but they are very happy here. Valentina's favourite place is the port, because the ships are beautiful.",
   vf=[("Valentina is sixteen.", False), ("She is from Antofagasta.", True), ("She is tall.", False),
       ("Her parents are doctors.", True), ("Her favourite place is the beach.", False)],
   preguntas=["How old is Valentina? => She is fifteen.", "Is she good at English? => Yes, she is.",
              "Why is the port her favourite place? => Because the ships are beautiful."]),
  dict(tipo="write", titulo="Write about you and your friend", instr="Escribe oraciones completas con el verbo to be.", items=[
   "My name", "I / years old", "My best friend", "He / She is (describe)", "We are"],
   modelo="My best friend is Javiera. She is funny and kind."),
 ]),

# ------------------------------------------------------------------ PRESENT SIMPLE
dict(slug="present-simple", titulo="Present Simple", nivel="1°", cefr="A1",
 objetivo="hablar de rutinas y hábitos con el presente simple.",
 goal="talk about routines and habits with the present simple.",
 recordar=[
  "I / You / We / They + <b>verbo</b>.  ·  He / She / It + <b>verbo + s</b>.",
  "Ortografía 3ª persona: watch → watch<b>es</b>, go → go<b>es</b>, study → stud<b>ies</b>, play → play<b>s</b>, have → <b>has</b>.",
  "Usamos el presente simple para rutinas, hábitos y verdades generales: <i>The sun rises in the east.</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the verb in the correct form", instr="Añade -s / -es / -ies cuando corresponda.", items=[
   "I [play] (play) football.", "She [watches] (watch) TV.", "He [goes] (go) to school.", "They [study] (study) English.",
   "We [live] (live) in Chile.", "My mother [cooks] (cook) dinner.", "The baby [cries] (cry) a lot.", "You [read] (read) books.",
   "He [has] (have) a dog.", "She [does] (do) her homework.", "The ship [leaves] (leave) at nine.", "My friends [swim] (swim) on Saturdays."]),
  dict(tipo="fill", titulo="Third person (add -s/-es/-ies)", instr="Escribe la 3ª persona singular del verbo.", items=[
   "go → he [goes]", "study → she [studies]", "watch → he [watches]", "play → she [plays]", "do → he [does]",
   "have → she [has]", "cry → it [cries]", "fix → he [fixes]", "wash → she [washes]", "fly → it [flies]",
   "work → he [works]", "kiss → she [kisses]"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la forma correcta.", items=[
   "My sister {like|likes*} pizza.", "We {go*|goes} to the beach in summer.", "The bus {arrive|arrives*} at 7:30.",
   "I {wake*|wakes} up early.", "Tom and Lucy {play*|plays} the guitar.", "The sailor {work|works*} on a ship.",
   "Water {boil|boils*} at 100 °C.", "You {speak*|speaks} English very well."]),
  dict(tipo="fill", titulo="Complete about daily routines", instr="Usa los verbos del recuadro en la forma correcta.", banco=["get", "brush", "take", "finish", "eat", "go", "do", "watch"], items=[
   "I [get] up at seven.", "My brother [brushes] his teeth after breakfast.", "We [take] the bus to school.",
   "School [finishes] at four.", "My dad [eats] lunch at work.", "They [go] to bed at eleven.",
   "She [does] her homework in the afternoon.", "My grandma [watches] the news at night."]),
  dict(tipo="text", titulo="Complete the text", instr="Escribe el verbo entre paréntesis en presente simple.", texto=
   "My name is Sofía. Every day I [wake] (wake) up at 6:30. I [have] (have) breakfast with my family. "
   "My brother [goes] (go) to school by bus. My mother [works] (work) in a shop near the port. "
   "My father [fixes] (fix) engines on fishing boats. In the evening we [watch] (watch) TV together. "
   "My father [cooks] (cook) dinner and my sister [does] (do) her homework. On Saturdays my family "
   "[visits] (visit) my grandparents. I [love] (love) my routine!"),
  dict(tipo="rewrite", titulo="Correct the mistake", instr="Reescribe la oración corregida (tercera persona).", cols=2, items=[
   "She go to school. => She goes to school.", "He watch TV. => He watches TV.", "My mother cook dinner. => My mother cooks dinner.",
   "The baby cry. => The baby cries.", "He have a dog. => He has a dog.", "She study English. => She studies English.",
   "It rain a lot. => It rains a lot.", "He do his homework. => He does his homework."]),
  dict(tipo="rewrite", titulo="Change the subject", instr="Reescribe la oración con el nuevo sujeto.", cols=2, items=[
   "I play basketball. (Carlos) => Carlos plays basketball.", "We study at night. (My sister) => My sister studies at night.",
   "They wash the car. (He) => He washes the car.", "You go to the gym. (She) => She goes to the gym.",
   "I have a bike. (My friend) => My friend has a bike.", "We fly to Santiago. (The plane) => The plane flies to Santiago."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras para formar oraciones.", items=[
   "My father works on a ship.", "I take the bus at seven.", "She studies English every day.",
   "We play football on Sundays.", "The ferry leaves at noon.", "He watches movies at night."]),
  dict(tipo="reading", titulo="Read about Captain López", instr="Lee el texto y responde.", titulo_texto="A day at sea", texto=
   "Captain López works on a cargo ship. He gets up at five o'clock every morning. He drinks a cup of coffee and checks the weather. "
   "At six, he talks to the crew and they start their work. The ship carries containers from Valparaíso to other countries. "
   "Captain López eats lunch at twelve with the crew. In the afternoon, he writes reports. At night, he calls his family "
   "because he misses them. He loves his job, but he likes holidays at home too.",
   vf=[("Captain López gets up at six.", False), ("He checks the weather in the morning.", True),
       ("The ship carries containers.", True), ("He eats lunch alone.", False), ("He calls his family at night.", True)],
   preguntas=["What does he drink in the morning? => He drinks a cup of coffee.",
              "What does he do in the afternoon? => He writes reports.",
              "Why does he call his family? => Because he misses them."]),
  dict(tipo="write", titulo="Now, write about YOUR routine", instr="Escribe 5 oraciones sobre tu rutina diaria.", items=[
   "Every day I", "In the morning I", "My mother / father", "After school I", "At night I"]),
 ]),
]
