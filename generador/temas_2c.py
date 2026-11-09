# 2° Medio (A2) — Gramática, parte C
TEMAS = [
# ------------------------------------------------------------------ PAST IRREGULAR
dict(slug="past-irregular", titulo="Past Simple: Irregular Verbs", nivel="2°", cefr="A2",
 objetivo="usar los verbos irregulares más frecuentes en pasado simple.",
 goal="use common irregular verbs in the past simple.",
 recordar=[
  "Los verbos irregulares no llevan -ed; hay que aprenderlos: <i>go → <b>went</b>, have → <b>had</b>, see → <b>saw</b></i>",
  "be → was/were · buy → bought · come → came · do → did · drink → drank · eat → ate · find → found · get → got · give → gave",
  "know → knew · leave → left · make → made · meet → met · put → put · read → read · run → ran · say → said · take → took · write → wrote",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the past form", instr="Escribe el pasado del verbo irregular.", items=[
   "go → [went]", "have → [had]", "see → [saw]", "eat → [ate]", "buy → [bought]", "take → [took]", "make → [made]", "come → [came]",
   "get → [got]", "write → [wrote]", "drink → [drank]", "leave → [left]", "meet → [met]", "give → [gave]", "find → [found]", "swim → [swam]"]),
  dict(tipo="match", titulo="Match the verb and its past", instr="Une el verbo con su pasado.", pares=[
   ("think", "thought"), ("speak", "spoke"), ("sleep", "slept"), ("sell", "sold"), ("wear", "wore"), ("break", "broke"), ("teach", "taught"), ("fly", "flew")]),
  dict(tipo="fill", titulo="Complete the sentences", instr="Escribe el verbo en pasado.", items=[
   "We [went] (go) to Viña on Saturday.", "I [saw] (see) a whale!", "She [bought] (buy) new shoes.", "They [ate] (eat) empanadas.",
   "He [wrote] (write) a letter.", "The ship [left] (leave) at midnight.", "I [had] (have) a great time.", "My dad [made] (make) a cake.",
   "We [met] (meet) a famous captain.", "She [took] (take) many photos."]),
  dict(tipo="classify", titulo="Regular or irregular?", instr="Escribe el pasado en la columna correcta.", categorias={
   "REGULAR": ["walked", "played", "visited", "studied", "arrived"], "IRREGULAR": ["went", "ran", "brought", "sang", "drove"]}),
  dict(tipo="text", titulo="Complete the story", instr="Escribe los verbos en pasado.", texto=
   "Last summer, my family and I [went] (go) to Chiloé. We [took] (take) the ferry from Pargua. On the ferry, I [saw] (see) dolphins! "
   "When we [got] (get) to Ancud, we [ate] (eat) curanto and [drank] (drink) fresh juice. The next day we [visited] (visit) the penguins. "
   "My sister [bought] (buy) a wool sweater and I [found] (find) a beautiful shell. We [came] (come) back home very happy."),
  dict(tipo="rewrite", titulo="Present to past", instr="Cambia la oración al pasado.", cols=2, items=[
   "I go to school by bus. => I went to school by bus.", "She has breakfast at 7. => She had breakfast at 7.", "We see the ships. => We saw the ships.",
   "He runs on the beach. => He ran on the beach.", "They give me a present. => They gave me a present.", "I make my bed. => I made my bed."]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "I goed to the port. => I went to the port.", "She buyed a car. => She bought a car.", "We eated pizza. => We ate pizza.",
   "He taked the bus. => He took the bus.", "They seed a film. => They saw a film.", "I writed a poem. => I wrote a poem."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "We saw a big cruise ship yesterday.", "My father bought fresh fish at the market.", "I met my best friend in 2019.", "They left the port at six o'clock."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="The Esmeralda", texto=
   "In 2023, my class went on a visit to the training ship Esmeralda. An officer met us at the port and took us on a tour. "
   "We saw the masts, the sails and the cabins of the cadets. The officer told us about the ship's long trips around the world. "
   "At the end, we had lunch on the deck and we ate fish with rice. I took a lot of photos. It was the best school trip!",
   vf=[("The class went to the Esmeralda.", True), ("A cadet met them at the port.", False), ("They saw the masts and the sails.", True), ("They ate chicken.", False)],
   preguntas=["What did the officer tell them about? => About the ship's long trips around the world.", "Where did they have lunch? => On the deck."]),
  dict(tipo="write", titulo="Your best trip", instr="Escribe sobre un viaje o paseo usando verbos irregulares.", items=[
   "Last … I went to", "I went with", "We saw", "We ate", "It was … because"]),
 ]),

# ------------------------------------------------------------------ PAST NEGATIVE & QUESTIONS
dict(slug="past-neg", titulo="Past Simple: Negativo y Preguntas", nivel="2°", cefr="A2",
 objetivo="formar oraciones negativas y preguntas en pasado simple con did / didn't.",
 goal="make negative sentences and questions in the past simple.",
 recordar=[
  "<b>Negativo:</b> sujeto + <b>didn't</b> + verbo base → <i>I didn't go. She didn't play.</i> (no: <i>didn't went</i>)",
  "<b>Pregunta:</b> <b>Did</b> + sujeto + verbo base? → <i>Did you go?</i> → Yes, I did. / No, I didn't.",
  "Wh-: <i>Where <b>did</b> you go? What <b>did</b> she buy? When <b>did</b> they arrive?</i>",
 ],
 ejercicios=[
  dict(tipo="rewrite", titulo="Make negative sentences", instr="Escribe en negativo.", cols=2, items=[
   "I went to the party. => I didn't go to the party.", "She played tennis. => She didn't play tennis.", "We saw the film. => We didn't see the film.",
   "He ate the cake. => He didn't eat the cake.", "They visited Chiloé. => They didn't visit Chiloé.", "The ship arrived. => The ship didn't arrive.",
   "I bought a jacket. => I didn't buy a jacket.", "You did your homework. => You didn't do your homework."]),
  dict(tipo="fill", titulo="Complete the questions and answers", instr="Completa con Did / did / didn't.", cols=1, items=[
   "[Did] you study for the test? — Yes, I [did].", "[Did] she call you? — No, she [didn't].", "[Did] they win the match? — Yes, they [did].",
   "[Did] he go to school yesterday? — No, he [didn't].", "[Did] the ferry leave on time? — Yes, it [did]."]),
  dict(tipo="rewrite", titulo="Write Yes/No questions", instr="Escribe la pregunta en pasado.", cols=2, items=[
   "you / watch the match => Did you watch the match?", "she / buy a phone => Did she buy a phone?", "they / go to the beach => Did they go to the beach?",
   "he / see the whale => Did he see the whale?", "your parents / call you => Did your parents call you?", "it / rain yesterday => Did it rain yesterday?"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I didn't {went|go*} out.", "{Did*|Do} you like the film?", "She didn't {saw|see*} me.", "Where did you {buy*|bought} it?",
   "{Did*|Was} he play football?", "They {didn't*|weren't} come.", "What {did*|do} you do last night?", "Did she {wrote|write*} the essay?"]),
  dict(tipo="rewrite", titulo="Write Wh- questions", instr="Escribe la pregunta para la parte en negrita.", cols=1, items=[
   "I went <b>to La Serena</b>. => Where did you go?", "She bought <b>a dress</b>. => What did she buy?", "They arrived <b>at 10 p.m.</b> => What time did they arrive?",
   "We went <b>by train</b>. => How did you go?", "He called <b>his grandmother</b>. => Who did he call?", "I left <b>because I was tired</b>. => Why did you leave?"]),
  dict(tipo="text", titulo="Complete the dialogue", instr="Completa con did, didn't o el verbo en la forma correcta.", texto=
   "MATEO: Hi Isi! [Did] you have a good weekend?\nISIDORA: Yes, I [did]! I [went] (go) to Santiago with my family.\nMATEO: Cool! What [did] you do there?\n"
   "ISIDORA: We [visited] (visit) a museum and we [ate] (eat) in a nice restaurant.\nMATEO: [Did] you see the Costanera Tower?\n"
   "ISIDORA: No, we [didn't]. We [didn't] (not) have time. And you? What did you [do]?\nMATEO: Nothing special. I [stayed] (stay) at home."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "I didn't went. => I didn't go.", "Did you saw it? => Did you see it?", "She don't come yesterday. => She didn't come yesterday.",
   "Where you went? => Where did you go?", "He didn't played. => He didn't play.", "Did they arrived? => Did they arrive?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "What did you eat for breakfast?", "We didn't see any dolphins.", "Did your brother pass the exam?", "Why didn't you call me?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A bad day", texto=
   "Yesterday was a terrible day for Benjamín. His alarm didn't ring, so he didn't have breakfast. He ran to the bus stop, but the bus didn't stop. "
   "He arrived at school at 9:15. He didn't bring his English book and the teacher wasn't happy. At lunch, he didn't have money. "
   "Fortunately, his friend Agustina shared her sandwich with him.",
   vf=[("Benjamín had breakfast.", False), ("The bus didn't stop.", True), ("He brought his English book.", False), ("Agustina shared her sandwich.", True)],
   preguntas=["Why didn't he have breakfast? => Because his alarm didn't ring.", "What time did he arrive at school? => At 9:15."]),
  dict(tipo="write", titulo="Interview a classmate", instr="Escribe 4 preguntas sobre el fin de semana y la respuesta de tu compañero.", items=[
   "Did you", "Where did you", "What did you", "Who did you"]),
 ]),

# ------------------------------------------------------------------ COUNTABLE / UNCOUNTABLE
dict(slug="countable-uncountable", titulo="Countable & Uncountable Nouns", nivel="2°", cefr="A2",
 objetivo="distinguir sustantivos contables e incontables y usar a / an / some correctamente.",
 goal="use countable and uncountable nouns correctly.",
 recordar=[
  "<b>Contables</b>: se pueden contar, tienen plural → <i>an apple, two apples, a ship, three ships</i>",
  "<b>Incontables</b>: no tienen plural ni a / an → <i>water, rice, milk, money, bread, information, advice, furniture, music</i>",
  "Para contar incontables: <i>a <b>bottle</b> of water, a <b>slice</b> of bread, a <b>kilo</b> of rice, a <b>cup</b> of tea, a <b>piece</b> of advice</i>",
  "Incontables van con verbo singular: <i>The water <b>is</b> cold. Money <b>isn't</b> everything.</i>",
 ],
 ejercicios=[
  dict(tipo="classify", titulo="Countable or uncountable?", instr="Clasifica las palabras.", categorias={
   "COUNTABLE": ["egg", "banana", "chair", "ship", "coin", "sandwich"], "UNCOUNTABLE": ["sugar", "milk", "money", "bread", "information", "music"]}),
  dict(tipo="fill", titulo="A, AN or SOME?", instr="Completa con a, an o some.", items=[
   "[an] orange", "[some] water", "[a] tomato", "[some] cheese", "[an] egg", "[some] rice", "[a] sandwich", "[some] milk",
   "[some] money", "[an] onion", "[some] bread", "[a] bottle"]),
  dict(tipo="match", titulo="Match the containers", instr="Une el envase o medida con el alimento.", pares=[
   ("a bottle of", "water"), ("a slice of", "pizza"), ("a cup of", "tea"), ("a kilo of", "potatoes"), ("a carton of", "milk"),
   ("a bar of", "chocolate"), ("a loaf of", "bread"), ("a can of", "tuna")]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "The water {is*|are} cold.", "I need {an advice|some advice*}.", "These apples {is|are*} delicious.", "I have {a|some*} homework today.",
   "{Is*|Are} there any milk?", "The information {is*|are} on the board.", "I bought two {breads|loaves of bread*}.", "My hair {is*|are} long."]),
  dict(tipo="fill", titulo="Plural or no plural?", instr="Escribe la palabra en plural si es contable; si es incontable, escríbela igual.", items=[
   "two (ship) → [ships]", "some (rice) → [rice]", "many (egg) → [eggs]", "a lot of (money) → [money]", "three (child) → [children]", "some (music) → [music]",
   "five (potato) → [potatoes]", "some (furniture) → [furniture]"]),
  dict(tipo="text", titulo="Complete the shopping list text", instr="Completa con a, an, some, is o are.", texto=
   "Today I'm going to the supermarket. We need [some] bread and [a] bottle of oil. There [isn't] any milk, so I need to buy [a] carton of milk. "
   "I also want [an] avocado and [some] tomatoes for a salad. The tomatoes at the market [are] very cheap this week. "
   "The cheese [is] expensive, so I'm not buying it."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "I need an information. => I need some information.", "The breads are fresh. => The bread is fresh.", "She has a lot of moneys. => She has a lot of money.",
   "I want a water. => I want some water / a bottle of water.", "The furnitures are new. => The furniture is new.", "Can you give me an advice? => Can you give me some advice?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "I'd like a cup of coffee, please.", "There is some cheese in the fridge.", "We need two kilos of rice.", "The news is very good today."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Supplies for the ship", texto=
   "Before a long trip, the cook of a ship buys a lot of food. For a crew of 20 people and one month at sea, he needs about 200 kilos of rice, "
   "300 kilos of potatoes, 100 litres of milk and 2,000 eggs. He also buys flour to make bread every day, a lot of coffee and some chocolate bars for special days. "
   "Fresh water is very important too; the ship makes its own water from the sea.",
   vf=[("The cook needs 2,000 eggs.", True), ("He buys bread every day at a shop.", False), ("He buys chocolate for special days.", True), ("The ship can make water.", True)],
   preguntas=["How many kilos of potatoes does he need? => 300 kilos.", "What does he make with the flour? => Bread."]),
  dict(tipo="write", titulo="Your fridge", instr="Escribe qué hay y qué no hay en tu refrigerador.", items=[
   "In my fridge there is some", "There are some", "There isn't any", "We need to buy a … of"]),
 ]),

# ------------------------------------------------------------------ QUANTIFIERS
dict(slug="quantifiers", titulo="Quantifiers: some / any / much / many", nivel="2°", cefr="A2",
 objetivo="usar cuantificadores con sustantivos contables e incontables.",
 goal="use some, any, much, many, a lot of, a few and a little.",
 recordar=[
  "<b>some</b> → afirmativo y ofrecimientos (<i>Would you like some tea?</i>) · <b>any</b> → negativo y preguntas",
  "<b>many</b> + contables (<i>How many ships?</i>) · <b>much</b> + incontables (<i>How much water?</i>) · <b>a lot of</b> → ambos",
  "<b>a few</b> + contables (algunos, pocos) · <b>a little</b> + incontables (un poco)",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Some or any?", instr="Completa con some o any.", items=[
   "There are [some] apples in the bag.", "We don't have [any] bread.", "Is there [any] milk?", "I have [some] friends in Peru.",
   "Would you like [some] cake?", "There aren't [any] boats today.", "Do you have [any] questions?", "She bought [some] flowers."]),
  dict(tipo="fill", titulo="Much or many?", instr="Completa con much o many.", items=[
   "How [many] students are there?", "How [much] money do you have?", "There isn't [much] time.", "I don't have [many] friends here.",
   "How [much] sugar do you want?", "There aren't [many] ships today.", "How [many] languages do you speak?", "We don't drink [much] coffee."]),
  dict(tipo="choice", titulo="A few or a little?", instr="Encierra la opción correcta.", items=[
   "I have {a few*|a little} cousins.", "Add {a few|a little*} salt.", "There are {a few*|a little} people here.", "Can I have {a few|a little*} water?",
   "She speaks {a few|a little*} English.", "I bought {a few*|a little} eggs."]),
  dict(tipo="choice", titulo="Choose the correct quantifier", instr="Encierra la opción correcta.", items=[
   "There are {much|a lot of*} tourists in summer.", "We don't have {some|any*} homework.", "How {much*|many} is this jacket?", "There's {a few|a little*} juice left.",
   "I saw {many*|much} dolphins.", "Is there {any*|some} ice?", "He doesn't eat {much*|many} meat.", "I need {some*|any} help."]),
  dict(tipo="rewrite", titulo="Write the question", instr="Escribe la pregunta con How much o How many.", cols=2, items=[
   "I have three brothers. => How many brothers do you have?", "It costs 5,000 pesos. => How much does it cost?", "I drink two litres of water. => How much water do you drink?",
   "There are 30 students. => How many students are there?", "We need one kilo of rice. => How much rice do we need?", "She has four cats. => How many cats does she have?"]),
  dict(tipo="text", titulo="Complete the dialogue", instr="Completa con some, any, much, many, a few, a little, a lot of.", texto=
   "MUM: We're making a cake. Do we have [any] eggs?\nSON: Yes, but only [a few] — three, I think.\nMUM: That's OK. How [much] flour is there?\n"
   "SON: There's [a lot of] flour, two kilos!\nMUM: Great. And sugar?\nSON: Only [a little]. And there isn't [any] butter.\n"
   "MUM: OK, I'll buy [some] butter. How [many] guests are coming?\nSON: Ten!"),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "How many money do you have? => How much money do you have?", "There aren't some chairs. => There aren't any chairs.", "I have much friends. => I have a lot of friends.",
   "Can I have a few milk? => Can I have a little milk?", "Is there some sugar? => Is there any sugar?", "There is a little people. => There are a few people."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "How many ships are in the port?", "There isn't much time left.", "I have a few questions for you.", "Would you like some tea?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="The fishing village", texto=
   "Caleta El Membrillo is a small fishing village in Valparaíso. There aren't many houses, but there are a lot of colourful boats. "
   "Every morning, a few fishermen go out to sea. When they come back, there are many people waiting to buy fish. "
   "There isn't much space, so the restaurants are small. You can eat some delicious fried fish there. In winter there aren't any tourists.",
   vf=[("There are many houses.", False), ("There are a lot of colourful boats.", True), ("The restaurants are very big.", False), ("There aren't any tourists in winter.", True)],
   preguntas=["Who goes out to sea every morning? => A few fishermen.", "What can you eat there? => Some delicious fried fish."]),
  dict(tipo="write", titulo="Describe your city or school", instr="Escribe oraciones con cuantificadores.", items=[
   "In my city there are a lot of", "There aren't many", "There isn't much", "There are a few"]),
 ]),
]
