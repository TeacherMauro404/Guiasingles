# 1° Medio (A1) — Gramática, parte C
TEMAS = [
# ------------------------------------------------------------------ PLURAL NOUNS
dict(slug="plural-nouns", titulo="Plural Nouns", nivel="1°", cefr="A1",
 objetivo="formar plurales regulares (-s, -es, -ies, -ves) e irregulares.",
 goal="make regular and irregular plural nouns.",
 recordar=[
  "Regla general <b>+s</b>: ship → ships · Terminados en s, sh, ch, x, o <b>+es</b>: box → boxes, potato → potatoes",
  "Consonante + y → <b>-ies</b>: city → cities (pero vocal + y → +s: boy → boys) · f / fe → <b>-ves</b>: knife → knives",
  "Irregulares: man → <b>men</b>, woman → <b>women</b>, child → <b>children</b>, person → <b>people</b>, foot → <b>feet</b>, tooth → <b>teeth</b>, mouse → <b>mice</b>, fish → <b>fish</b>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the plural", instr="Escribe el plural de cada sustantivo.", items=[
   "boat → [boats]", "bus → [buses]", "city → [cities]", "box → [boxes]", "knife → [knives]", "day → [days]",
   "watch → [watches]", "baby → [babies]", "dish → [dishes]", "leaf → [leaves]", "tomato → [tomatoes]", "key → [keys]",
   "wife → [wives]", "beach → [beaches]", "party → [parties]", "toy → [toys]"]),
  dict(tipo="fill", titulo="Irregular plurals", instr="Escribe el plural irregular.", items=[
   "man → [men]", "woman → [women]", "child → [children]", "person → [people]", "foot → [feet]", "tooth → [teeth]",
   "mouse → [mice]", "fish → [fish]", "sheep → [sheep]", "goose → [geese]"]),
  dict(tipo="classify", titulo="Classify the plurals", instr="Escribe el plural de cada palabra en la columna correcta.", categorias={
   "+ S": ["ships", "boys", "maps"], "+ ES": ["glasses", "foxes", "lunches"], "- IES": ["countries", "ladies", "stories"], "- VES": ["wolves", "lives", "halves"]}),
  dict(tipo="fill", titulo="Complete the sentences", instr="Escribe el plural de la palabra entre paréntesis.", items=[
   "There are three [ships] (ship) in the port.", "I have two [brothers] (brother).", "The [children] (child) are playing.",
   "My [feet] (foot) are cold.", "We need five [boxes] (box).", "Those [women] (woman) are doctors.",
   "Valparaíso has many [stairs] (stair).", "The [babies] (baby) are sleeping.", "Brush your [teeth] (tooth)!", "I love [stories] (story)."]),
  dict(tipo="choice", titulo="Choose the correct plural", instr="Encierra el plural correcto.", items=[
   "two {mans|men*}", "three {potatos|potatoes*}", "four {citys|cities*}", "five {wolfs|wolves*}", "many {people*|peoples}",
   "six {churchs|churches*}", "two {monkeys*|monkies}", "ten {fishes|fish*}"]),
  dict(tipo="rewrite", titulo="Make the sentences plural", instr="Cambia la oración al plural.", cols=2, items=[
   "The ship is big. => The ships are big.", "A child is playing. => Children are playing.", "The box is heavy. => The boxes are heavy.",
   "This city is beautiful. => These cities are beautiful.", "The woman is a captain. => The women are captains.", "My tooth is white. => My teeth are white."]),
  dict(tipo="text", titulo="Complete the text", instr="Escribe el plural de las palabras entre paréntesis.", texto=
   "In the port of Valparaíso there are many [ships] (ship) and [boats] (boat). Every day, [men] (man) and [women] (woman) work there. "
   "They carry [boxes] (box) and check the [containers] (container). Tourists take [photos] (photo) of the colourful [houses] (house) on the hills. "
   "[Children] (child) eat ice cream and [families] (family) walk along the coast."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el plural incorrecto.", cols=2, items=[
   "I have two foots. => I have two feet.", "The citys are big. => The cities are big.", "There are three childs. => There are three children.",
   "I need two knifes. => I need two knives.", "Many persons are here. => Many people are here.", "The boxs are red. => The boxes are red."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="The fish market", texto=
   "Every Saturday, my family goes to the fish market in Caleta Portales. There are many boats and many fishermen. "
   "The men and women sell fish, crabs and shellfish. Some children help their parents. There are also cats and seagulls waiting for food. "
   "We usually buy two kilos of fish and some potatoes for lunch.",
   vf=[("The family goes to the market on Sundays.", False), ("Men and women sell fish.", True), ("Some children help their parents.", True), ("They buy two kilos of meat.", False)],
   preguntas=["What animals wait for food? => Cats and seagulls.", "What do they buy for lunch? => Two kilos of fish and some potatoes."]),
  dict(tipo="write", titulo="Your turn", instr="Escribe oraciones con sustantivos en plural.", items=[
   "In my classroom there are", "In my house there are", "At the port you can see"]),
 ]),

# ------------------------------------------------------------------ DEMONSTRATIVES
dict(slug="demonstratives", titulo="This / That / These / Those", nivel="1°", cefr="A1",
 objetivo="usar los demostrativos para objetos cercanos y lejanos, en singular y plural.",
 goal="use this, that, these and those to point at things.",
 recordar=[
  "Cerca (here): <b>this</b> + singular · <b>these</b> + plural  →  <i>this book, these books</i>",
  "Lejos (there): <b>that</b> + singular · <b>those</b> + plural  →  <i>that ship, those ships</i>",
  "Con el verbo to be: <i>This <b>is</b> my pen. These <b>are</b> my pens. Is that your bag? Are those your shoes?</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="This or These?", instr="Objetos cerca: escribe this o these.", items=[
   "[This] pencil", "[These] notebooks", "[This] apple", "[These] shoes", "[This] map", "[These] keys", "[This] chair", "[These] people"]),
  dict(tipo="fill", titulo="That or Those?", instr="Objetos lejos: escribe that o those.", items=[
   "[That] ship", "[Those] boats", "[That] lighthouse", "[Those] birds", "[That] house", "[Those] mountains", "[That] man", "[Those] children"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "{This*|These} is my phone.", "{That|Those*} are my friends over there.", "{These*|This} cookies are delicious.",
   "Look at {that*|those} big ship!", "{Is*|Are} this your jacket?", "{Are*|Is} those your shoes?",
   "{This|These*} are my parents.", "{That*|Those} car is very old.", "Who is {that*|those} girl?", "I like {these*|this} trousers."]),
  dict(tipo="rewrite", titulo="Change to plural", instr="Cambia la oración al plural.", cols=2, items=[
   "This is my book. => These are my books.", "That is a boat. => Those are boats.", "This chair is new. => These chairs are new.",
   "That girl is my sister. => Those girls are my sisters.", "Is this your pen? => Are these your pens?", "That box is heavy. => Those boxes are heavy."]),
  dict(tipo="rewrite", titulo="Change to singular", instr="Cambia la oración al singular.", cols=2, items=[
   "These are my keys. => This is my key.", "Those are cats. => That is a cat.", "These apples are red. => This apple is red.",
   "Those men are sailors. => That man is a sailor."]),
  dict(tipo="text", titulo="Complete the dialogue", instr="Completa con this, that, these o those.", texto=
   "SHOP ASSISTANT: Hello! Can I help you?\nTOMÁS: Yes, please. How much is [this] T-shirt here?\nSHOP ASSISTANT: It's 8,000 pesos.\n"
   "TOMÁS: And [those] jeans over there?\nSHOP ASSISTANT: [Those] jeans are 20,000 pesos.\nTOMÁS: OK. And [these] socks here?\n"
   "SHOP ASSISTANT: [These] are 2,000 pesos. And [that] jacket on the wall is on sale!\nTOMÁS: Great! I'll take [this] T-shirt and [that] jacket."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "These is my bag. => This is my bag.", "This are my friends. => These are my friends.", "Those car is red. => That car is red.",
   "That are my shoes. => Those are my shoes.", "Is these your phone? => Is this your phone?", "I like this boots. => I like these boots."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "Those ships are from Panama.", "Is this your notebook?", "These are my new shoes.", "That lighthouse is very old."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Photos of my trip", texto=
   "Look at these photos of my trip to Chiloé! This is my mother and this is my little brother. These houses are called palafitos. "
   "That is the church of Castro. It is very old. Those boats are from the fishermen of the island. And that dog over there is our new friend, Chocolate!",
   vf=[("The trip was to Chiloé.", True), ("The houses are called palafitos.", True), ("The church is new.", False), ("The dog's name is Chocolate.", True)],
   preguntas=["Who are the people in the first photo? => Her mother and her little brother.", "Whose boats are those? => They are from the fishermen of the island."]),
  dict(tipo="write", titulo="Your turn", instr="Escribe sobre objetos de tu sala (cerca y lejos).", items=[
   "This is", "These are", "That is", "Those are"]),
 ]),

# ------------------------------------------------------------------ THERE IS / THERE ARE
dict(slug="there-is-are", titulo="There is / There are", nivel="1°", cefr="A1",
 objetivo="describir lugares y cantidades con there is / there are.",
 goal="describe places using there is and there are.",
 recordar=[
  "<b>There is</b> (there's) + singular / incontable: <i>There is a ship. There is some water.</i>",
  "<b>There are</b> + plural: <i>There are two ships.</i>",
  "Negativo: <b>There isn't</b> a… / <b>There aren't any</b>…  ·  Pregunta: <b>Is there</b> a…? / <b>Are there any</b>…?  → Yes, there is. / No, there aren't.",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Complete with there is or there are", instr="Completa con there is o there are.", largo=True, items=[
   "[There is] a computer in the lab.", "[There are] thirty students in my class.", "[There is] a lighthouse near the port.",
   "[There are] many hills in Valparaíso.", "[There is] some milk in the fridge.", "[There are] two windows in my room.",
   "[There is] a dog in the garden.", "[There are] three ships in the bay."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "{There is*|There are} a bank on this street.", "{There is|There are*} five apples on the table.", "{Is there*|Are there} a pool at your school?",
   "{Is there|Are there*} any restaurants near here?", "There {isn't*|aren't} a museum in my town.", "There {isn't|aren't*} any chairs.",
   "{There's*|There are} an elevator in the building.", "Are there any boats? Yes, there {is|are*}."]),
  dict(tipo="rewrite", titulo="Make negative sentences", instr="Escribe en negativo.", cols=2, items=[
   "There is a TV. => There isn't a TV.", "There are some books. => There aren't any books.", "There is a park. => There isn't a park.",
   "There are two boats. => There aren't two boats.", "There is some sugar. => There isn't any sugar.", "There are many people. => There aren't many people."]),
  dict(tipo="rewrite", titulo="Make questions and answer", instr="Escribe la pregunta y la respuesta corta.", cols=2, items=[
   "a library / school (Yes) => Is there a library at school? Yes, there is.", "computers / the lab (Yes) => Are there any computers in the lab? Yes, there are.",
   "a cinema / your town (No) => Is there a cinema in your town? No, there isn't.", "ships / the port (Yes) => Are there any ships in the port? Yes, there are.",
   "a pool / your house (No) => Is there a pool in your house? No, there isn't.", "students / the gym (No) => Are there any students in the gym? No, there aren't."]),
  dict(tipo="text", titulo="Complete the description", instr="Completa con there is, there are, there isn't o there aren't.", texto=
   "My school is near the sea. [There is] a big building with three floors. [There are] twenty classrooms and [there is] a workshop for engines. "
   "[There is] a library on the first floor, but [there isn't] a swimming pool. In the yard [there are] some trees and benches. "
   "[There aren't] any shops inside the school, but [there is] a small kiosk where we buy snacks."),
  dict(tipo="match", titulo="Match questions and answers", instr="Une cada pregunta con su respuesta.", pares=[
   ("Is there a hospital near here?", "Yes, there is. It's on Prat Street."), ("Are there any chairs?", "No, there aren't. Sit on the floor."),
   ("How many students are there?", "There are thirty-two."), ("Is there any juice?", "No, there isn't. There's water."),
   ("Are there any ships today?", "Yes, there are three cruise ships.")]),
  dict(tipo="rewrite", titulo="How many…? Write questions and answers", instr="Escribe la pregunta con How many … are there? y responde.", cols=1, items=[
   "students / your class (32) => How many students are there in your class? There are thirty-two.",
   "days / a week (7) => How many days are there in a week? There are seven.",
   "players / a football team (11) => How many players are there in a football team? There are eleven.",
   "regions / Chile (16) => How many regions are there in Chile? There are sixteen."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "There are two ferries in the bay.", "Is there a bathroom here?", "There isn't any bread at home.", "Are there any good restaurants?", "There is a map on the wall."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Plaza Sotomayor", texto=
   "Plaza Sotomayor is in the centre of Valparaíso. There is a big monument to the heroes of Iquique. There are many old buildings around the square, "
   "and one of them is the Navy building. There are also a lot of tourists and street vendors. There isn't a beach, but the port is very close. "
   "From the square, there are boats that take you on a tour of the bay.",
   vf=[("Plaza Sotomayor is in Viña del Mar.", False), ("There is a monument in the square.", True), ("There is a beach in the square.", False), ("There are tours of the bay.", True)],
   preguntas=["What building is there near the square? => There is the Navy building.", "Who is there in the square? => There are tourists and street vendors."]),
  dict(tipo="write", titulo="Describe your bedroom or your neighbourhood", instr="Escribe 5 oraciones.", items=[
   "In my bedroom there is", "There are", "There isn't", "There aren't any", "Is there"]),
 ]),

# ------------------------------------------------------------------ PRESENT SIMPLE NEG & QUESTIONS
dict(slug="present-simple-neg", titulo="Present Simple: Negativo y Preguntas", nivel="1°", cefr="A1",
 objetivo="formar oraciones negativas y preguntas en presente simple con do / does.",
 goal="make negative sentences and questions with do / does.",
 recordar=[
  "<b>Negativo:</b> I / You / We / They + <b>don't</b> + verbo · He / She / It + <b>doesn't</b> + verbo (¡sin -s!): <i>She doesn't like fish.</i>",
  "<b>Pregunta:</b> <b>Do</b> + I / you / we / they + verbo? · <b>Does</b> + he / she / it + verbo?  →  Yes, I do. / No, she doesn't.",
  "Wh- questions: <b>Where do</b> you live? <b>What does</b> he do? <b>When do</b> they study?",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Complete with don't or doesn't", instr="Completa con don't o doesn't.", items=[
   "I [don't] like coffee.", "She [doesn't] eat meat.", "We [don't] live in Santiago.", "He [doesn't] play tennis.",
   "They [don't] watch TV.", "My dog [doesn't] sleep much.", "You [don't] speak French.", "My father [doesn't] work on Sundays.",
   "The bus [doesn't] stop here.", "My friends [don't] have class today."]),
  dict(tipo="rewrite", titulo="Make negative sentences", instr="Transforma al negativo.", cols=2, items=[
   "I like pizza. => I don't like pizza.", "She plays the piano. => She doesn't play the piano.", "They live near the sea. => They don't live near the sea.",
   "He goes to the gym. => He doesn't go to the gym.", "We study French. => We don't study French.", "It rains in summer. => It doesn't rain in summer.",
   "My mother drives. => My mother doesn't drive.", "The ship leaves today. => The ship doesn't leave today."]),
  dict(tipo="fill", titulo="Complete the questions", instr="Completa con Do o Does y la respuesta corta.", cols=1, items=[
   "[Do] you like music? — Yes, I [do].", "[Does] your brother play football? — No, he [doesn't].", "[Do] they live in Viña? — Yes, they [do].",
   "[Does] she speak English? — Yes, she [does].", "[Does] the ferry leave at 8? — No, it [doesn't].", "[Do] we have a test? — No, we [don't]."]),
  dict(tipo="rewrite", titulo="Write questions", instr="Escribe la pregunta en presente simple.", cols=2, items=[
   "you / like / fish => Do you like fish?", "she / work / at the port => Does she work at the port?", "they / play / basketball => Do they play basketball?",
   "he / have / a car => Does he have a car?", "your parents / speak / English => Do your parents speak English?", "the class / start / at 8 => Does the class start at 8?"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "She doesn't {like*|likes} rice.", "{Do|Does*} he work here?", "We {don't*|doesn't} go out on Mondays.", "Does your cat {eat*|eats} fish?",
   "Where {do*|does} you live?", "What time {do|does*} the bus arrive?", "My parents {don't*|doesn't} smoke.", "{Do*|Does} your friends play games?"]),
  dict(tipo="match", titulo="Match questions and answers", instr="Une cada pregunta con la respuesta.", pares=[
   ("Where do you live?", "In Playa Ancha."), ("What does your father do?", "He's a mechanic."), ("When do you have English?", "On Tuesdays."),
   ("Does she like music?", "Yes, she does."), ("What time do you get up?", "At half past six."), ("Do they study here?", "No, they don't.")]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "She don't like tea. => She doesn't like tea.", "He doesn't plays. => He doesn't play.", "Do she live here? => Does she live here?",
   "They doesn't work. => They don't work.", "Does he likes it? => Does he like it?", "I not speak German. => I don't speak German."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "Does your mother work on Saturdays?", "I don't eat breakfast at home.", "Where do your grandparents live?", "My brother doesn't like fish."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde con oraciones completas.", titulo_texto="Two different friends", texto=
   "Bruno and Simón are best friends, but they are very different. Bruno gets up early and goes running. Simón doesn't like sport; he plays video games. "
   "Bruno doesn't eat meat, but Simón loves hamburgers. Simón doesn't study much, but he is very creative. "
   "They don't go to the same school, but they meet every Friday at the beach.",
   vf=[("Simón likes sport.", False), ("Bruno doesn't eat meat.", True), ("They go to the same school.", False), ("They meet on Fridays.", True)],
   preguntas=["Does Bruno get up early? => Yes, he does.", "What does Simón play? => He plays video games.", "Where do they meet? => They meet at the beach."]),
  dict(tipo="write", titulo="About you", instr="Escribe 2 cosas que NO haces y 2 preguntas para un compañero.", items=[
   "I don't", "My best friend doesn't", "Do you", "Does your"]),
 ]),

# ------------------------------------------------------------------ OBJECT PRONOUNS
dict(slug="object-pronouns", titulo="Object Pronouns", nivel="1°", cefr="A1",
 objetivo="usar los pronombres objeto (me, you, him, her, it, us, them) después del verbo o preposición.",
 goal="use object pronouns after verbs and prepositions.",
 recordar=[
  "I → <b>me</b> · you → <b>you</b> · he → <b>him</b> · she → <b>her</b> · it → <b>it</b> · we → <b>us</b> · they → <b>them</b>",
  "Sujeto ANTES del verbo, objeto DESPUÉS: <i><b>She</b> loves <b>him</b>. <b>He</b> loves <b>her</b>.</i>",
  "Después de preposiciones: <i>with me, for them, to us, about her</i>.",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the object pronoun", instr="Escribe el pronombre objeto.", items=[
   "I → [me]", "you → [you]", "he → [him]", "she → [her]", "it → [it]", "we → [us]", "they → [them]"]),
  dict(tipo="fill", titulo="Replace the words in bold", instr="Escribe el pronombre objeto que reemplaza las palabras en negrita.", items=[
   "I love <b>my mother</b>. → [her]", "Call <b>Pedro</b>. → [him]", "I can't find <b>my keys</b>. → [them]", "She likes <b>the song</b>. → [it]",
   "Help <b>Ana and me</b>! → [us]", "We visit <b>our grandparents</b>. → [them]", "Ask <b>the teacher</b> (man). → [him]", "I see <b>the ship</b>. → [it]"]),
  dict(tipo="choice", titulo="Choose the correct pronoun", instr="Encierra la opción correcta.", items=[
   "Can you help {I|me*}?", "{She*|Her} is my friend.", "I like {they|them*}.", "Give the book to {he|him*}.", "{We*|Us} play together.",
   "This present is for {she|her*}.", "Come with {we|us*}!", "{They*|Them} live near me.", "Look at {it*|its}!", "Tell {me*|my} the truth."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con me, you, him, her, it, us o them.", texto=
   "I have a best friend called Rocío. I see [her] every day at school. Her brother Felipe is funny; we play football with [him] on Saturdays. "
   "Rocío has two cats. She loves [them] very much. Yesterday her mother made a cake and gave [it] to [us]. "
   "Rocío always helps [me] with English. And you? Who helps [you]?"),
  dict(tipo="rewrite", titulo="Rewrite with object pronouns", instr="Reemplaza las palabras en negrita.", cols=2, items=[
   "I know <b>Laura</b>. => I know her.", "She calls <b>her brothers</b>. => She calls them.", "We watch <b>the film</b>. => We watch it.",
   "They visit <b>Tomás</b>. => They visit him.", "He helps <b>my friend and me</b>. => He helps us.", "I read <b>the books</b>. => I read them."]),
  dict(tipo="classify", titulo="Subject or object?", instr="Clasifica los pronombres.", categorias={
   "SUBJECT": ["I", "he", "she", "we", "they"], "OBJECT": ["me", "him", "her", "us", "them"]}),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "She loves he. => She loves him.", "Me am tired. => I am tired.", "Call I later. => Call me later.",
   "I don't know they. => I don't know them.", "Him is my cousin. => He is my cousin.", "Come with we. => Come with us."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My teacher helps us with English.", "Do you know him?", "I bought it for her.", "They always call me at night."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A message from Martina", texto=
   "Hi Lucas! Are you free on Saturday? My parents are taking me and my sister to Quintero. We want you to come with us! "
   "My dad has a new boat and he wants to show it to everyone. My grandparents are coming too. You know them, they are very nice. "
   "Please call me tonight. See you! Martina",
   vf=[("Martina is going to Quintero.", True), ("Her mother has a new boat.", False), ("Lucas knows the grandparents.", True), ("Martina wants Lucas to send an email.", False)],
   preguntas=["Who is taking Martina to Quintero? => Her parents.", "What does her dad want to show? => His new boat."]),
  dict(tipo="write", titulo="Your turn", instr="Escribe oraciones con pronombres objeto.", items=[
   "My best friend helps me", "I love my family because they", "My favourite singer is … I listen to"]),
 ]),
]
