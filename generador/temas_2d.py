# 2° Medio (A2) — Gramática, parte D
TEMAS = [
# ------------------------------------------------------------------ COMPARATIVES
dict(slug="comparatives", titulo="Comparatives", nivel="2°", cefr="A2",
 objetivo="comparar dos personas, lugares u objetos con adjetivos comparativos.",
 goal="compare two things using comparative adjectives.",
 recordar=[
  "Adjetivos cortos: <b>+er than</b> → <i>tall → taller than</i> · terminados en -e: <i>large → larger</i> · CVC: <i>big → bigger</i> · -y: <i>easy → easier</i>",
  "Adjetivos largos (2+ sílabas): <b>more … than</b> → <i>more expensive than, more interesting than</i>",
  "Irregulares: good → <b>better</b> · bad → <b>worse</b> · far → <b>farther / further</b>",
  "Igualdad: <b>as … as</b> → <i>Viña is as beautiful as Valparaíso.</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the comparative form", instr="Escribe el comparativo.", items=[
   "tall → [taller]", "big → [bigger]", "easy → [easier]", "large → [larger]", "hot → [hotter]", "happy → [happier]",
   "expensive → [more expensive]", "good → [better]", "bad → [worse]", "interesting → [more interesting]", "fast → [faster]", "dangerous → [more dangerous]"]),
  dict(tipo="classify", titulo="Classify by rule", instr="Escribe el comparativo en la columna correcta.", categorias={
   "+ER": ["cheaper", "older", "colder"], "DOUBLE + ER": ["thinner", "wetter", "fatter"], "-IER": ["busier", "funnier", "heavier"], "MORE …": ["more modern", "more beautiful", "more famous"]}),
  dict(tipo="fill", titulo="Complete the sentences", instr="Usa el comparativo + than.", largo=True, items=[
   "A ship is [bigger than] (big) a boat.", "Summer is [hotter than] (hot) winter.", "English is [easier than] (easy) Chinese.", "A car is [more expensive than] (expensive) a bike.",
   "My grade is [better than] (good) yours.", "Today is [worse than] (bad) yesterday.", "Santiago is [busier than] (busy) Valparaíso.", "Math is [more difficult than] (difficult) Art."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "My brother is {taller*|more tall} than me.", "This film is {more boring*|boringer} than the book.", "She is {gooder|better*} at English.",
   "A plane is faster {that|than*} a train.", "Today is {hoter|hotter*} than yesterday.", "Chile is {longer*|more long} than Peru.", "This test was {worse*|badder}."]),
  dict(tipo="rewrite", titulo="Compare", instr="Escribe una oración comparativa.", cols=1, items=[
   "the Pacific / the Atlantic (big) => The Pacific is bigger than the Atlantic.", "a ferry / a cargo ship (small) => A ferry is smaller than a cargo ship.",
   "a phone / a laptop (cheap) => A phone is cheaper than a laptop.", "football / chess (exciting) => Football is more exciting than chess.",
   "Arica / Punta Arenas (warm) => Arica is warmer than Punta Arenas.", "my cousin / me (old) => My cousin is older than me."]),
  dict(tipo="fill", titulo="As … as", instr="Completa con as … as o not as … as.", largo=True, items=[
   "Ana is 15. Sofía is 15. Ana is [as old as] Sofía.", "The bus is slow. The train is fast. The bus is [not as fast as] the train.",
   "My bag is 5 kg. Your bag is 5 kg. My bag is [as heavy as] yours.", "Viña is beautiful. Valparaíso is beautiful too. Viña is [as beautiful as] Valparaíso."]),
  dict(tipo="text", titulo="Complete the comparison", instr="Escribe el comparativo de los adjetivos.", texto=
   "Valparaíso and Viña del Mar are neighbours, but they are very different. Valparaíso is [older] (old) than Viña and its streets are [steeper] (steep). "
   "Viña is [more modern] (modern) and its beaches are [larger] (large). Many tourists think Valparaíso is [more interesting] (interesting) because of its history. "
   "In summer, Viña is [busier] (busy) than Valparaíso. Which city is [better] (good)? I can't decide!"),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "She is more tall than me. => She is taller than me.", "This is more cheap. => This is cheaper.", "He is gooder than me. => He is better than me.",
   "It's biger than mine. => It's bigger than mine.", "Gold is expensiver than silver. => Gold is more expensive than silver.", "I'm older that you. => I'm older than you."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Two ships", texto=
   "The Esmeralda and the Juan Sebastián de Elcano are two famous training ships. The Esmeralda, from Chile, is 113 metres long. "
   "The Elcano, from Spain, is about the same length, but it is older: it was built in 1927, and the Esmeralda was launched in 1953. "
   "Interestingly, both ships were built in the same Spanish city, Cádiz. Many Chileans think the Esmeralda is more elegant, but Spanish people say the Elcano is more beautiful!",
   vf=[("The Esmeralda is from Spain.", False), ("The Elcano is older than the Esmeralda.", True), ("Both ships were built in Cádiz.", True), ("The Elcano is much longer than the Esmeralda.", False)],
   preguntas=["When was the Esmeralda launched? => In 1953.", "Where were both ships built? => In Cádiz, Spain."]),
  dict(tipo="write", titulo="Compare", instr="Escribe 4 comparaciones.", items=[
   "Me and my best friend:", "Summer and winter:", "My city and Santiago:", "Cats and dogs:"]),
 ]),

# ------------------------------------------------------------------ SUPERLATIVES
dict(slug="superlatives", titulo="Superlatives", nivel="2°", cefr="A2",
 objetivo="expresar el grado máximo con superlativos (the -est / the most).",
 goal="use superlative adjectives to talk about extremes.",
 recordar=[
  "Adjetivos cortos: <b>the + -est</b> → <i>tall → the tallest</i> · <i>big → the biggest</i> · <i>happy → the happiest</i>",
  "Adjetivos largos: <b>the most</b> → <i>the most beautiful, the most expensive</i>",
  "Irregulares: good → <b>the best</b> · bad → <b>the worst</b> · far → <b>the farthest</b>",
  "Usamos <b>in</b> con lugares/grupos: <i>the tallest boy <b>in</b> the class</i> · <b>of</b> con períodos: <i>the best day <b>of</b> my life</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the superlative", instr="Escribe el superlativo con the.", items=[
   "tall → [the tallest]", "big → [the biggest]", "happy → [the happiest]", "nice → [the nicest]", "good → [the best]", "bad → [the worst]",
   "expensive → [the most expensive]", "hot → [the hottest]", "famous → [the most famous]", "easy → [the easiest]", "long → [the longest]", "important → [the most important]"]),
  dict(tipo="fill", titulo="Comparative and superlative", instr="Completa la tabla.", cols=1, items=[
   "small → [smaller] → [the smallest]", "heavy → [heavier] → [the heaviest]", "beautiful → [more beautiful] → [the most beautiful]",
   "good → [better] → [the best]", "fat → [fatter] → [the fattest]", "bad → [worse] → [the worst]"]),
  dict(tipo="fill", titulo="Complete the sentences", instr="Usa el superlativo.", largo=True, items=[
   "The Pacific is [the largest] (large) ocean in the world.", "Ojos del Salado is [the highest] (high) volcano in the world.", "This is [the best] (good) day of my life!",
   "Mario is [the funniest] (funny) student in the class.", "That was [the worst] (bad) film ever.", "Valparaíso has [the most colourful] (colourful) hills in Chile.",
   "Antarctica is [the coldest] (cold) continent.", "The cheetah is [the fastest] (fast) land animal."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "She is the {smartest*|most smart} girl in the class.", "It's the {most expensive*|expensivest} car.", "He is the {best*|goodest} player.",
   "This is the {biggest*|bigest} ship in the port.", "It's the coldest month {of*|in} the year.", "He is the tallest boy {of|in*} the school."]),
  dict(tipo="match", titulo="World records", instr="Une el récord con su respuesta.", pares=[
   ("The longest river in the world", "the Nile / the Amazon"), ("The biggest animal", "the blue whale"), ("The driest desert", "the Atacama Desert"),
   ("The highest mountain", "Mount Everest"), ("The largest country", "Russia"), ("The smallest country", "Vatican City")]),
  dict(tipo="text", titulo="Complete the text", instr="Escribe el superlativo de los adjetivos.", texto=
   "Chile is a country of records. The Atacama Desert is [the driest] (dry) desert in the world. Ojos del Salado is [the highest] (high) active volcano on Earth. "
   "The Carretera Austral is one of [the most beautiful] (beautiful) roads in South America. Rapa Nui is one of [the most isolated] (isolated) inhabited islands in the world. "
   "And for me, Valparaíso is [the best] (good) city in Chile!"),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "She's the most tall girl. => She's the tallest girl.", "It's the baddest day. => It's the worst day.", "He's the more intelligent. => He's the most intelligent.",
   "It's biggest city. => It's the biggest city.", "The best player of the team. => The best player in the team.", "The most cheap shop. => The cheapest shop."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "What is the longest river in Chile?", "My grandmother is the oldest person in my family.", "This is the most interesting museum in the city.", "December is the hottest month of the year."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Giants of the sea", texto=
   "The blue whale is the largest animal that has ever lived. It can be 30 metres long and weigh 150 tonnes. Its heart is as big as a small car! "
   "The fastest fish in the ocean is the sailfish; it can swim at 110 km/h. The deepest part of the ocean is the Mariana Trench, almost 11 kilometres deep. "
   "And the oldest animal? A Greenland shark can live more than 400 years!",
   vf=[("The blue whale is the largest animal ever.", True), ("The fastest fish is the shark.", False), ("The Mariana Trench is the deepest place.", True), ("Greenland sharks live 40 years.", False)],
   preguntas=["How fast can the sailfish swim? => 110 km/h.", "How big is the blue whale's heart? => As big as a small car."]),
  dict(tipo="write", titulo="Your opinion", instr="Escribe tu opinión con superlativos.", items=[
   "The best film is", "The most interesting subject is", "The worst food is", "The most beautiful place in Chile is"]),
 ]),

# ------------------------------------------------------------------ PREPOSITIONS OF TIME
dict(slug="prepositions-time", titulo="Prepositions of Time: in / on / at", nivel="2°", cefr="A2",
 objetivo="usar in, on y at con expresiones de tiempo.",
 goal="use in, on and at with time expressions.",
 recordar=[
  "<b>AT</b> → horas y momentos precisos: <i>at 7 o'clock, at noon, at night, at the weekend, at Christmas</i>",
  "<b>ON</b> → días y fechas: <i>on Monday, on 18th September, on my birthday, on Friday morning</i>",
  "<b>IN</b> → meses, años, estaciones, partes del día, períodos: <i>in May, in 2025, in summer, in the morning, in the 20th century</i>",
  "Sin preposición: <i>today, tomorrow, yesterday, next week, last year, every day, this morning</i>",
 ],
 ejercicios=[
  dict(tipo="classify", titulo="IN, ON or AT?", instr="Clasifica las expresiones.", categorias={
   "IN": ["July", "winter", "2010", "the evening"], "ON": ["Tuesday", "my birthday", "21st May", "Sunday afternoon"], "AT": ["9 o'clock", "midnight", "Christmas", "lunchtime"]}),
  dict(tipo="fill", titulo="Complete with in, on or at", instr="Completa con la preposición correcta.", items=[
   "My birthday is [in] October.", "We have English [on] Monday.", "The ship leaves [at] 6:30.", "I was born [in] 2010.",
   "It's cold [in] winter.", "I sleep [at] night.", "We celebrate [on] 18th September.", "I study [in] the afternoon.",
   "The film starts [at] eight.", "We go to the beach [in] summer.", "See you [on] Friday!", "Shops close [at] Christmas."]),
  dict(tipo="choice", titulo="Preposition or nothing?", instr="Encierra la opción correcta (– = sin preposición).", items=[
   "I'll see you {on|–*} tomorrow.", "We went to Chiloé {in*|on} 2022.", "I have a test {–*|on} next week.", "She calls me {at*|in} night.",
   "We met {–*|in} last year.", "He works {on*|in} Saturday mornings.", "Class finishes {at*|on} 4:30.", "I go to the gym {–*|in} every day."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con in, on, at o – (sin preposición).", texto=
   "The Naval Glories Day is [on] 21st May. It remembers the Battle of Iquique, which happened [in] 1879. "
   "[In] the morning, there is a big parade in Valparaíso. It usually starts [at] ten o'clock. "
   "[At] midday, the President gives a speech. Many families come [in] the afternoon to see the ships. This year I'm going with my class!"),
  dict(tipo="rewrite", titulo="Answer the questions", instr="Responde con oraciones completas.", cols=1, items=[
   "When is your birthday? => My birthday is on …", "What time do you get up on weekdays? => I get up at …",
   "When do you go on holiday? => I go on holiday in …", "When were you born? => I was born in …"]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige la preposición.", cols=2, items=[
   "I was born on 2009. => I was born in 2009.", "See you in Monday. => See you on Monday.", "The class starts on 8:00. => The class starts at 8:00.",
   "I study at the morning. => I study in the morning.", "We met on last week. => We met last week.", "It's hot on summer. => It's hot in summer."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "We have a test on Thursday.", "The ship arrives at midnight.", "It usually rains in June.", "My parents got married in 2005."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="The school calendar", texto=
   "At our school, classes start in March and finish in December. The winter holidays are in July — two weeks. "
   "On the 21st of May we have a ceremony for the Navy. In September we celebrate the Fiestas Patrias with a big party on the 17th. "
   "The graduation of 4° Medio is in November, at seven in the evening.",
   vf=[("Classes start in March.", True), ("The winter holidays are in August.", False), ("The Navy ceremony is on 21st May.", True), ("The graduation is in the morning.", False)],
   preguntas=["When is the Fiestas Patrias party? => On the 17th of September.", "When is the graduation? => In November, at seven in the evening."]),
  dict(tipo="write", titulo="Your year", instr="Escribe oraciones con in / on / at.", items=[
   "My favourite day is … because on", "In summer I", "At the weekend I", "On my birthday I"]),
 ]),
]
