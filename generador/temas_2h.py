# 2° Medio (A2) — Vocabulario, parte C y lectura
TEMAS = [
# ------------------------------------------------------------------ HOUSE
dict(slug="house", titulo="House & Furniture", nivel="2°", cefr="A2",
 objetivo="nombrar las partes de la casa y los muebles, y describir una vivienda.",
 goal="describe a house, its rooms and furniture.",
 recordar=[
  "Rooms: living room, kitchen, bedroom, bathroom, dining room, garage, garden, balcony, hall, stairs, upstairs / downstairs",
  "Furniture: sofa, armchair, bed, wardrobe, desk, shelf, table, chair, fridge, cooker, washing machine, sink, mirror, lamp, carpet",
  "Describir: <i>There is / There are…</i> · prepositions: <i>next to, opposite, between, upstairs</i> · Tipos: house, flat / apartment, cabin",
 ],
 ejercicios=[
  dict(tipo="classify", titulo="Where do you find it?", instr="Clasifica los objetos según la habitación.", categorias={
   "KITCHEN": ["fridge", "cooker", "sink", "microwave"], "BEDROOM": ["bed", "wardrobe", "pillow", "alarm clock"], "BATHROOM": ["shower", "toilet", "mirror", "towel"], "LIVING ROOM": ["sofa", "armchair", "TV", "carpet"]}),
  dict(tipo="match", titulo="Match the words", instr="Une la palabra con su traducción.", pares=[
   ("wardrobe", "ropero / clóset"), ("shelf", "repisa"), ("cooker", "cocina (artefacto)"), ("stairs", "escalera"), ("pillow", "almohada"),
   ("washing machine", "lavadora"), ("armchair", "sillón"), ("roof", "techo")]),
  dict(tipo="fill", titulo="What room is it?", instr="Escribe la habitación.", items=[
   "You cook here. → [kitchen]", "You sleep here. → [bedroom]", "You take a shower here. → [bathroom]", "You watch TV and relax here. → [living room]",
   "You park the car here. → [garage]", "You eat dinner with your family here. → [dining room]", "There are plants and flowers here. → [garden]", "You go up and down here. → [stairs]"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "There {is*|are} a sofa in the living room.", "There {is|are*} two beds in my room.", "My bedroom is {upstairs*|up stairs}.", "The fridge is {in*|on} the kitchen.",
   "The lamp is {on*|in} the desk.", "My clothes are in the {wardrobe*|fridge}.", "We live in a {flat*|plane} on the 5th floor.", "There aren't {some|any*} chairs."]),
  dict(tipo="text", titulo="Complete the description", instr="Completa con palabras del recuadro.", banco=["view", "upstairs", "kitchen", "bedrooms", "living room", "stairs", "balcony", "garden"], texto=
   "I live in a typical house in Cerro Alegre. It's a colourful house with many [stairs] to the door. Downstairs, there is a [living room] with a big window and a small [kitchen]. "
   "[Upstairs], there are three [bedrooms] and a bathroom. My favourite place is the [balcony] because there's an amazing [view] of the bay. "
   "We don't have a [garden], but we have many plants."),
  dict(tipo="rewrite", titulo="Describe the room", instr="Escribe oraciones con there is / there are.", cols=2, items=[
   "a bed / my room => There is a bed in my room.", "two windows / the kitchen => There are two windows in the kitchen.",
   "some books / the shelf => There are some books on the shelf.", "a mirror / the bathroom => There is a mirror in the bathroom."]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "There are a sofa. => There is a sofa.", "The bed is in the kitchen. => The bed is in the bedroom.", "My room is up the stairs floor. => My room is upstairs.",
   "There is two lamps. => There are two lamps."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "There is a big wardrobe in my bedroom.", "The bathroom is next to the kitchen.", "How many bedrooms are there in your house?", "We have a small garden with flowers."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el aviso y responde.", titulo_texto="FOR RENT — Flat in Playa Ancha", texto=
   "Modern flat on the 4th floor with a beautiful sea view. It has two bedrooms, one bathroom, a living-dining room and a small kitchen with a new cooker and fridge. "
   "There is a balcony, but there isn't a garden. The building has a lift and a garage. It's near the university and the bus stop. Price: 450,000 pesos per month. No pets.",
   vf=[("The flat is on the 4th floor.", True), ("It has three bedrooms.", False), ("There is a garden.", False), ("You can have a dog.", False)],
   preguntas=["What is near the flat? => The university and the bus stop.", "How much is the rent? => 450,000 pesos per month."]),
  dict(tipo="write", titulo="Your dream house", instr="Describe tu casa ideal.", items=[
   "My dream house is in", "It has", "There is a … and there are", "My favourite room is … because"]),
 ]),

# ------------------------------------------------------------------ WEATHER
dict(slug="weather", titulo="Weather & Seasons", nivel="2°", cefr="A2",
 objetivo="describir el clima y las estaciones, y comprender un pronóstico del tiempo.",
 goal="talk about the weather, seasons and forecasts.",
 recordar=[
  "Sustantivo → adjetivo: sun → <b>sunny</b> · rain → <b>rainy</b> · cloud → <b>cloudy</b> · wind → <b>windy</b> · fog → <b>foggy</b> · snow → <b>snowy</b> · storm → <b>stormy</b>",
  "<i>What's the weather like?</i> → <i>It's sunny. It's raining. It's 18 degrees.</i> · hot, warm, cool, cold, freezing",
  "Seasons: spring, summer, autumn (fall), winter · Mar: calm sea, rough sea, waves, tide, swell (marejada)",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Noun to adjective", instr="Escribe el adjetivo.", items=[
   "sun → [sunny]", "rain → [rainy]", "cloud → [cloudy]", "wind → [windy]", "fog → [foggy]", "snow → [snowy]", "storm → [stormy]", "ice → [icy]"]),
  dict(tipo="fill", titulo="Order the temperatures", instr="Escribe la palabra según la temperatura.", items=[
   "35 °C → [hot]", "22 °C → [warm]", "12 °C → [cool]", "4 °C → [cold]", "-5 °C → [freezing]"]),
  dict(tipo="match", titulo="Match the weather and the item", instr="¿Qué necesitas?", pares=[
   ("It's raining.", "an umbrella"), ("It's sunny and hot.", "sunglasses and sun cream"), ("It's freezing.", "a coat and gloves"), ("It's windy.", "a kite"),
   ("It's snowy.", "boots"), ("The sea is rough.", "stay in the port")]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "{What's*|How's} the weather like?", "It's {rain|raining*} now.", "In winter it's {cold*|hot} in Punta Arenas.", "It's very {fog|foggy*} today.",
   "The leaves fall in {autumn*|spring}.", "It's 30 {degrees*|grades}.", "It {snows*|snowy} in the Andes.", "Christmas in Chile is in {summer*|winter}."]),
  dict(tipo="fill", titulo="Seasons in Chile", instr="Completa con la estación (hemisferio sur).", items=[
   "December, January, February → [summer]", "March, April, May → [autumn]", "June, July, August → [winter]", "September, October, November → [spring]"]),
  dict(tipo="text", titulo="Complete the weather forecast", instr="Completa con palabras del recuadro.", banco=["sunny", "degrees", "rain", "cloudy", "windy", "waves", "storm", "cold"], texto=
   "Good evening! Here is the weather forecast for the Valparaíso region. Tomorrow morning will be [cloudy] and foggy on the coast. "
   "In the afternoon it will be [sunny] and warm, with a maximum of 24 [degrees]. On Thursday, a [storm] is coming from the south. "
   "There will be heavy [rain] and it will be very [windy]. Fishermen should stay in the port because the [waves] will be up to four metres. "
   "The weekend will be [cold] but dry."),
  dict(tipo="rewrite", titulo="Describe the weather", instr="Escribe una oración sobre el clima.", cols=2, items=[
   "Valparaíso / foggy / morning => It's foggy in Valparaíso in the morning.", "Santiago / hot / summer => It's hot in Santiago in summer.",
   "Puerto Montt / rain / a lot => It rains a lot in Puerto Montt.", "the Atacama / dry / always => It's always dry in the Atacama."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "What's the weather like today?", "It's going to rain this afternoon.", "Spring is my favourite season.", "The sea was very rough yesterday."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Marejadas", texto=
   "In Chile, 'marejadas' (big swells) are common, especially in winter. They happen when storms far away in the Pacific Ocean create big waves that travel to our coast. "
   "During a marejada, the sea is very rough and waves can be more than five metres high. The Navy closes the ports and small boats can't go out. "
   "People must stay away from the beaches and rocks. Marejadas can damage roads and buildings near the sea.",
   vf=[("Marejadas are common in winter.", True), ("They come from storms near the beach.", False), ("The Navy closes the ports.", True), ("People can swim during a marejada.", False)],
   preguntas=["How high can the waves be? => More than five metres.", "What can marejadas damage? => Roads and buildings near the sea."]),
  dict(tipo="write", titulo="Your favourite season", instr="Escribe sobre el clima.", items=[
   "Today the weather is", "My favourite season is … because", "In winter in my city it is", "When it rains, I like to"]),
 ]),

# ------------------------------------------------------------------ READING: MY DAILY LIFE
dict(slug="reading-daily-life", titulo="Reading: My Daily Life", nivel="2°", cefr="A2",
 objetivo="comprender textos breves sobre la vida diaria y responder preguntas de comprensión.",
 goal="read short texts about daily life and answer comprehension questions.",
 recordar=[
  "Estrategias: 1) Lee el título y predice el tema. 2) Lee una vez de forma general (skimming). 3) Busca información específica (scanning).",
  "Palabras clave en las preguntas: <b>who</b> (persona), <b>where</b> (lugar), <b>when / what time</b> (tiempo), <b>why</b> (razón → because).",
  "No necesitas entender todas las palabras: usa el contexto para deducir el significado.",
 ],
 ejercicios=[
  dict(tipo="reading", titulo="Text 1: Read and answer", instr="Lee el texto y responde.", titulo_texto="Catalina's week", texto=
   "Hi! I'm Catalina and I'm sixteen. I live in Quilpué with my parents and my little brother, Lucas. From Monday to Friday, I get up at 6:00 because I take the train to Valparaíso. "
   "The trip takes forty minutes, so I usually read or listen to music. My school is near the port. I study Tourism because I want to work on cruise ships one day. "
   "After school I have volleyball practice on Tuesdays and Thursdays. On Wednesdays I help my mother in her small bakery. "
   "At the weekend I sleep late, meet my friends and sometimes we go to the beach in Viña. I love my life, but I'm always tired on Fridays!",
   vf=[("Catalina lives in Valparaíso.", False), ("She takes the train to school.", True), ("The trip takes an hour.", False), ("She studies Tourism.", True),
       ("She has volleyball practice three times a week.", False), ("She is always tired on Fridays.", True)],
   preguntas=["Who does Catalina live with? => With her parents and her little brother, Lucas.", "Why does she get up at 6:00? => Because she takes the train to Valparaíso.",
              "What does she do on the train? => She reads or listens to music.", "What does she do on Wednesdays? => She helps her mother in her bakery."]),
  dict(tipo="match", titulo="Vocabulary in context", instr="Une cada palabra del texto 1 con su significado.", pares=[
   ("trip", "viaje / trayecto"), ("near", "cerca"), ("practice", "entrenamiento"), ("bakery", "panadería"), ("sleep late", "dormir hasta tarde"), ("one day", "algún día")]),
  dict(tipo="reading", titulo="Text 2: Read and answer", instr="Lee el texto y responde.", titulo_texto="A day in the life of a port pilot", texto=
   "Rodrigo Vera is a port pilot in Valparaíso. His job is to guide big ships safely into the port. He doesn't have a normal timetable: sometimes he works at night, "
   "sometimes early in the morning. When a ship arrives, a small boat takes Rodrigo to it. Then he climbs a rope ladder to get on the ship — it can be dangerous when the sea is rough! "
   "On the ship, he talks to the captain and gives instructions to park the ship. Rodrigo studied for many years and he speaks English every day, "
   "because captains come from all over the world. 'I love my job because every day is different,' he says.",
   vf=[("Rodrigo guides ships into the port.", True), ("He always works in the morning.", False), ("He climbs a rope ladder.", True), ("He never speaks English at work.", False)],
   preguntas=["How does Rodrigo get to the ship? => A small boat takes him to it.", "When is his job dangerous? => When the sea is rough.",
              "Why does he speak English every day? => Because captains come from all over the world.", "Why does he love his job? => Because every day is different."]),
  dict(tipo="fill", titulo="Find the words", instr="Busca en el texto 2 la palabra que significa…", items=[
   "horario → [timetable]", "escalera de cuerda → [rope ladder]", "peligroso → [dangerous]", "agitado (mar) → [rough]", "instrucciones → [instructions]", "estacionar → [park]"]),
  dict(tipo="classify", titulo="Compare Catalina and Rodrigo", instr="Clasifica las oraciones (C = Catalina, R = Rodrigo).", categorias={
   "CATALINA": ["takes the train", "plays volleyball", "helps in a bakery"], "RODRIGO": ["works at night", "climbs a ladder", "talks to captains"]}),
  dict(tipo="write", titulo="Your daily life", instr="Escribe un texto corto (6 oraciones) sobre tu vida diaria, como el de Catalina.", items=[
   "My name is … and I live in", "From Monday to Friday I", "After school I", "On Wednesdays I", "At the weekend I", "I love / I don't like"]),
 ]),
]
