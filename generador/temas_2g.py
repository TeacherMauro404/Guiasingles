# 2° Medio (A2) — Vocabulario, parte B y lectura
TEMAS = [
# ------------------------------------------------------------------ FOOD
dict(slug="food", titulo="Food & Drink", nivel="2°", cefr="A2",
 objetivo="nombrar alimentos y bebidas, describir hábitos alimenticios y pedir comida.",
 goal="talk about food, eating habits and ordering in a restaurant.",
 recordar=[
  "Groups: fruit (apple, grape, avocado) · vegetables (lettuce, onion, carrot) · meat (beef, chicken, pork) · seafood (fish, mussels, crab) · dairy (milk, cheese, yoghurt) · grains (rice, bread, pasta)",
  "Meals: breakfast · lunch · dinner / supper · snack · Adjetivos: delicious, tasty, spicy, sweet, salty, sour, healthy, junk food",
  "En el restaurante: <i>Can I see the menu, please? · I'd like… · Could I have…? · Can I have the bill, please?</i>",
 ],
 ejercicios=[
  dict(tipo="classify", titulo="Classify the food", instr="Clasifica los alimentos en su grupo.", categorias={
   "FRUIT": ["grapes", "pear", "lemon", "avocado"], "VEGETABLES": ["lettuce", "onion", "carrot", "corn"], "SEAFOOD": ["mussels", "salmon", "crab", "hake"], "DAIRY": ["cheese", "yoghurt", "butter", "milk"]}),
  dict(tipo="match", titulo="Match the Chilean dish and the description", instr="Une el plato con su descripción.", pares=[
   ("empanada de pino", "pastry filled with meat, onion, egg and olives"), ("pastel de choclo", "corn pie with meat and chicken"), ("caldillo de congrio", "conger eel soup"),
   ("sopaipilla", "fried pumpkin bread"), ("chorrillana", "chips with meat, onion and eggs"), ("completo", "hot dog with avocado and tomato")]),
  dict(tipo="fill", titulo="Describe the taste", instr="Completa con un adjetivo del recuadro.", banco=["sweet", "salty", "spicy", "sour", "healthy", "delicious"], items=[
   "Lemons are [sour].", "Chocolate is [sweet].", "Chips have a lot of salt. They're [salty].", "Chilli peppers are [spicy].", "Salads are [healthy].", "My grandma's cazuela is [delicious]!"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I'd {like*|liking} a glass of water.", "{Can*|Do} I have the bill, please?", "I usually have {a breakfast|breakfast*} at 7.", "Fruit {is*|are} good for you.",
   "Could I {have*|has} a menu?", "{How much*|How many} is the fish?", "I'm {hungry*|hunger}.", "Would you like {some*|any} dessert?"]),
  dict(tipo="text", titulo="Complete the restaurant dialogue", instr="Completa con palabras del recuadro.", banco=["menu", "like", "drink", "bill", "starter", "main course", "dessert", "Could"], texto=
   "WAITER: Good evening. Here's the [menu].\nCUSTOMER: Thank you. For a [starter], I'd like the shellfish soup.\nWAITER: And for the [main course]?\n"
   "CUSTOMER: I'd [like] the grilled hake with salad.\nWAITER: Anything to [drink]?\nCUSTOMER: A lemonade, please.\nWAITER: Would you like a [dessert]?\n"
   "CUSTOMER: No, thanks. [Could] I have the [bill], please?"),
  dict(tipo="rewrite", titulo="Order politely", instr="Transforma en un pedido educado (I'd like… / Could I have…?).", cols=2, items=[
   "Give me a coffee. => I'd like a coffee, please.", "I want the menu. => Could I have the menu, please?", "Bring me water. => Could I have some water, please?",
   "I want fish. => I'd like the fish, please."]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "I'd like a water. => I'd like a glass of water.", "The breads are fresh. => The bread is fresh.", "I like eat salad. => I like eating salad.",
   "How many is the cake? => How much is the cake?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "I usually have bread and avocado for breakfast.", "Could I have a glass of juice, please?", "Fish is healthier than red meat.", "What would you like for dessert?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A healthy diet for sailors", texto=
   "Working on a ship is hard, so sailors need a healthy diet. In the past, sailors on long trips didn't eat fresh fruit and many got a disease called scurvy. "
   "Today, ships carry fruit, vegetables and frozen food. A good diet on board includes fish, rice, beans, eggs and lots of water. "
   "Cooks try to avoid too much fried food and sugar, because sailors don't do much exercise on long trips.",
   vf=[("In the past, sailors ate a lot of fresh fruit.", False), ("Scurvy is a disease.", True), ("Ships carry frozen food today.", True), ("Cooks prepare a lot of fried food.", False)],
   preguntas=["Why do sailors need a healthy diet? => Because working on a ship is hard.", "Why do cooks avoid sugar and fried food? => Because sailors don't do much exercise on long trips."]),
  dict(tipo="write", titulo="Your eating habits", instr="Escribe sobre tus hábitos alimenticios.", items=[
   "For breakfast I usually have", "My favourite dish is", "I don't like", "I think I should eat more"]),
 ]),

# ------------------------------------------------------------------ CLOTHES
dict(slug="clothes", titulo="Clothes & Shopping", nivel="2°", cefr="A2",
 objetivo="nombrar prendas de vestir, describir ropa y desenvolverse al comprar.",
 goal="talk about clothes and go shopping in English.",
 recordar=[
  "Clothes: T-shirt, shirt, sweater/jumper, jacket, coat, jeans, trousers, shorts, skirt, dress, uniform, socks, shoes, trainers, boots, cap, scarf, gloves",
  "<b>wear</b> (llevar puesto): <i>I'm wearing a jacket.</i> · <b>put on / take off</b> (ponerse / quitarse) · Sizes: S, M, L, XL",
  "Comprar: <i>Can I help you? · Can I try it on? · What size are you? · How much is it / are they? · It's too big / small. · I'll take it.</i>",
 ],
 ejercicios=[
  dict(tipo="classify", titulo="Classify the clothes", instr="¿Para qué clima es cada prenda?", categorias={
   "HOT WEATHER": ["shorts", "sandals", "T-shirt", "cap"], "COLD WEATHER": ["coat", "scarf", "gloves", "boots"]}),
  dict(tipo="match", titulo="Match the words", instr="Une la prenda con su traducción.", pares=[
   ("trousers", "pantalones"), ("sweater", "chaleco / suéter"), ("skirt", "falda"), ("trainers", "zapatillas"), ("gloves", "guantes"), ("scarf", "bufanda"), ("coat", "abrigo")]),
  dict(tipo="fill", titulo="What do they wear?", instr="Completa con una prenda lógica.", items=[
   "A sailor wears a white [uniform].", "In winter I wear a warm [coat / jacket].", "On my feet I wear [socks] and [shoes].", "On the beach I wear [shorts / a swimsuit].",
   "When it's sunny, I wear a [cap / hat].", "For a wedding, she wears a long [dress]."]),
  dict(tipo="choice", titulo="Is or are? It or them?", instr="Encierra la opción correcta.", items=[
   "How much {is|are*} these jeans?", "How much {is*|are} this jacket?", "These shoes are nice. Can I try {it|them*} on?", "I love this dress. I'll take {it*|them}.",
   "Your trousers {is|are*} dirty.", "She {wears*|carries} glasses.", "It's cold. {Put on*|Take off} your jacket.", "These boots are too {small*|smalls}."]),
  dict(tipo="text", titulo="Complete the shopping dialogue", instr="Completa con palabras del recuadro.", banco=["help", "size", "try", "changing rooms", "too", "much", "take", "cash"], texto=
   "ASSISTANT: Hello, can I [help] you?\nCLIENT: Yes, I'm looking for a jacket.\nASSISTANT: What [size] are you?\nCLIENT: Medium. Can I [try] this one on?\n"
   "ASSISTANT: Of course. The [changing rooms] are over there.\n…\nCLIENT: It's [too] big. Do you have a small?\nASSISTANT: Yes, here you are.\n"
   "CLIENT: Perfect! How [much] is it?\nASSISTANT: It's 35,000 pesos.\nCLIENT: OK, I'll [take] it. Can I pay in [cash]?"),
  dict(tipo="rewrite", titulo="What are they wearing?", instr="Escribe con el presente continuo.", cols=1, items=[
   "Pedro / a blue shirt and jeans => Pedro is wearing a blue shirt and jeans.", "Ana / a red dress and black shoes => Ana is wearing a red dress and black shoes.",
   "the cadets / white uniforms => The cadets are wearing white uniforms.", "I / (describe your clothes now) => I am wearing …"]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "How much is these shoes? => How much are these shoes?", "I'm wearing a trousers. => I'm wearing trousers.", "Can I try on it? => Can I try it on?",
   "This jeans are cheap. => These jeans are cheap.", "She is weared a hat. => She is wearing a hat.", "It's too much big. => It's too big."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "Can I try these trainers on?", "What size are you?", "I'm wearing my school uniform.", "This jacket is too expensive."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="The cadet's uniform", texto=
   "At the Naval School, cadets have different uniforms. For classes, they wear a dark blue uniform with a white shirt and black shoes. "
   "For ceremonies, they wear a white uniform, white gloves and a special cap. When they sail on the training ship, they wear comfortable trousers, "
   "a sweater and boots. In winter, they also wear a thick coat because the sea wind is very cold.",
   vf=[("For classes they wear a white uniform.", False), ("They wear white gloves for ceremonies.", True), ("On the ship they wear boots.", True), ("They don't need a coat in winter.", False)],
   preguntas=["What do they wear for ceremonies? => A white uniform, white gloves and a special cap.", "Why do they wear a thick coat in winter? => Because the sea wind is very cold."]),
  dict(tipo="write", titulo="Your clothes", instr="Escribe sobre tu ropa.", items=[
   "Today I'm wearing", "My favourite clothes are", "At the weekend I usually wear", "I never wear"]),
 ]),

# ------------------------------------------------------------------ DAILY ROUTINES
dict(slug="daily-routines", titulo="Daily Routines", nivel="2°", cefr="A2",
 objetivo="describir la rutina diaria con verbos, horas y conectores de secuencia.",
 goal="describe your daily routine with times and sequence words.",
 recordar=[
  "wake up · get up · take a shower · get dressed · brush my teeth · have breakfast · go to school · have lunch · do homework · have dinner · go to bed",
  "Conectores: <b>first</b>, <b>then</b>, <b>after that</b>, <b>next</b>, <b>finally</b> · <i>before / after + -ing: after having breakfast…</i>",
  "Presente simple + hora: <i>I get up <b>at</b> 6:30. She has lunch <b>at</b> one o'clock.</i>",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the verb and the complement", instr="Une para formar actividades de rutina.", pares=[
   ("wake", "up"), ("take", "a shower"), ("brush", "my teeth"), ("get", "dressed"), ("have", "breakfast"), ("do", "homework"), ("go", "to bed"), ("catch", "the bus")]),
  dict(tipo="fill", titulo="Complete the routine", instr="Usa los verbos del recuadro en presente simple.", banco=["wakes up", "gets dressed", "has", "takes", "catches", "starts", "does", "goes"], items=[
   "Sofía [wakes up] at 6:00.", "She [takes] a shower.", "She [gets dressed] in her uniform.", "She [has] breakfast with her mother.",
   "She [catches] the bus at 7:00.", "Classes [start] at 8:00.", "In the afternoon she [does] her homework.", "She [goes] to bed at 10:30."]),
  dict(tipo="fill", titulo="Sequence words", instr="Completa con first, then, after that o finally.", items=[
   "[First], I wake up.", "[Then], I take a shower.", "[After that], I have breakfast.", "[Finally], I go to school."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I {get*|gets} up at seven.", "He {brush|brushes*} his teeth.", "We have lunch {at*|in} one o'clock.", "She {do|does*} her homework at night.",
   "After {have|having*} breakfast, I go to school.", "My dad {go|goes*} to work by car.", "I {don't*|doesn't} watch TV in the morning.", "What time {do*|does} you go to bed?"]),
  dict(tipo="text", titulo="Complete the text", instr="Escribe los verbos en presente simple (3ª persona).", texto=
   "Don Manuel is a fisherman in Caleta Portales. He [wakes] (wake) up at 4:00 a.m. First, he [drinks] (drink) a cup of tea. Then he [goes] (go) to the beach "
   "and [prepares] (prepare) his boat. He [fishes] (fish) until ten o'clock. After that, he [sells] (sell) the fish at the market. "
   "In the afternoon, he [repairs] (repair) his nets and [rests] (rest). Finally, he [goes] (go) to bed at 9:00 p.m."),
  dict(tipo="rewrite", titulo="Write questions about the text", instr="Escribe preguntas sobre don Manuel y respóndelas.", cols=1, items=[
   "What time / wake up? => What time does he wake up? He wakes up at 4:00 a.m.", "What / drink first? => What does he drink first? He drinks a cup of tea.",
   "Where / sell the fish? => Where does he sell the fish? At the market.", "What time / go to bed? => What time does he go to bed? At 9:00 p.m."]),
  dict(tipo="order", titulo="Put the routine in order", instr="Ordena las palabras.", items=[
   "I always brush my teeth after breakfast.", "My sister takes a shower at night.", "What time do you have dinner?", "After school I do my homework."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A day on the training ship", texto=
   "On the training ship, cadets have a strict routine. They get up at 6:00 and make their beds. Then they do exercise on the deck for twenty minutes. "
   "After that, they have breakfast at 7:00. In the morning they have classes about navigation and safety. They have lunch at 12:30. "
   "In the afternoon, they clean the ship and practise with the sails. They have dinner at 7:00 p.m. and go to bed at 10:00 p.m.",
   vf=[("Cadets get up at 7:00.", False), ("They exercise on the deck.", True), ("They have navigation classes in the afternoon.", False), ("They go to bed at 10:00 p.m.", True)],
   preguntas=["What do they do after getting up? => They make their beds.", "What do they do in the afternoon? => They clean the ship and practise with the sails."]),
  dict(tipo="write", titulo="Your routine", instr="Describe tu rutina con conectores y horas.", items=[
   "First, I", "Then, I", "After that, I", "In the afternoon, I", "Finally, I"]),
 ]),
]
