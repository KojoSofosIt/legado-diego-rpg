"""World content: rooms, items, creatures, NPCs."""

ROOMS = {
    # ── MUNDO MORTAL ──────────────────────────────────────────────────────────
    "altar_diego": {
        "name": "Altar de Diego",
        "description": (
            "Una choza humilde al borde del pueblo. El olor a copal llena el cuarto. "
            "Sobre un altar de piedra volcánica descansan flores de cempasúchil y una foto "
            "descolorida de un guerrero con dos sangres en el rostro. "
            "Citlali está sentada junto al fuego, mirándote."
        ),
        "exits": {"norte": "plaza_pueblo", "este": "casa_citlali"},
        "items": [],
        "creatures": [],
        "npcs": ["citlali"],
        "features": {
            "altar":  "Foto de Diego: hombre alto, ojos claros, espada de obsidiana al cinto.",
            "copal":  "Brasas de copal que dibujan espirales que no siguen el viento.",
            "flores": "Cempasúchil fresco. Alguien lo renueva cada día.",
        },
    },

    "plaza_pueblo": {
        "name": "Plaza de Tlacopan",
        "description": (
            "La plaza central. Un ahuehuete centenario da sombra a una fuente seca. "
            "Los vecinos te evitan con la mirada, pero te observan. "
            "Al norte el camino se adentra en las barrancas."
        ),
        "exits": {"sur": "altar_diego", "norte": "camino_barrancas", "este": "mercado"},
        "items": [],
        "creatures": [],
        "npcs": ["rodrigo"],
        "features": {
            "ahuehuete": "El árbol viejo tiene marcas de garras en la corteza — demasiado altas para un perro.",
            "fuente":    "Seca desde hace décadas. En el fondo hay una moneda negra con un cráneo.",
        },
    },

    "casa_citlali": {
        "name": "Casa de Citlali",
        "description": (
            "Estantes hasta el techo con frascos, raíces y cosas que prefieren no nombrarse. "
            "En el centro, sobre un petate, tres objetos aguardan: "
            "una espada de obsidiana, un arcabuz con plumas de quetzal y un escudo de piel de jaguar."
        ),
        "exits": {"oeste": "altar_diego"},
        "items": ["tlachicotl", "tonatiuh", "escudo_ceiba", "copal_sagrado"],
        "creatures": [],
        "npcs": [],
        "features": {
            "espada":  "Tlachicotl. La hoja refleja algo que no está en el cuarto.",
            "arcabuz": "Tonatiuh. Plumas de quetzal descoloridas. Huele a pólvora vieja y copal.",
            "escudo":  "Escudo Ceiba. Piel de jaguar sobre madera sagrada. Emite calor al tocarlo.",
            "frascos": "Docenas de frascos con etiquetas en náhuatl. Citlali sabe exactamente qué hay en cada uno.",
        },
    },

    "mercado": {
        "name": "Mercado del Pueblo",
        "description": (
            "Tres puestos bajo un techo de palma. La vendedora te mira con ojo clínico — "
            "ya sabe quién eres. Tiene hierbas medicinales en el mostrador."
        ),
        "exits": {"oeste": "plaza_pueblo"},
        "items": ["hierbas_curativas"],
        "creatures": [],
        "npcs": ["vendedora"],
        "features": {
            "puestos": "Hierbas, velas, amuletos. Nada de armas — esas las guarda Citlali.",
        },
    },

    "camino_barrancas": {
        "name": "Camino a las Barrancas",
        "description": (
            "El sendero se estrecha y los árboles se cierran sobre tu cabeza. "
            "El aire huele a tierra mojada y a algo metálico, como sangre vieja. "
            "Las barrancas esperan al norte."
        ),
        "exits": {"sur": "plaza_pueblo", "norte": "barrancas_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "arboles":  "Marcas en la corteza: círculos y espirales que Diego dejó en su tiempo.",
            "sendero":  "Huellas en el barro. Una de ellas tiene forma de mano humana.",
        },
    },

    # ── BARRANCAS DEL COBRE ───────────────────────────────────────────────────
    "barrancas_entrada": {
        "name": "Entrada a las Barrancas",
        "description": (
            "Paredes de roca rojiza se alzan veinte metros a cada lado. "
            "El eco no funciona como debería — tus pasos regresan con retraso. "
            "Un fragmento de obsidiana brilla entre las piedras del suelo."
        ),
        "exits": {"sur": "camino_barrancas", "norte": "claro_bosque", "este": "ribera_rio"},
        "items": ["fragmento_obsidiana"],
        "creatures": [],
        "npcs": [],
        "features": {
            "paredes":  "Roca volcánica con petroglifos: figuras que se transforman de animal a humano.",
            "eco":      "Tu voz regresa cambiada. No del todo como la mandaste.",
        },
    },

    "ribera_rio": {
        "name": "Ribera del Río Oscuro",
        "description": (
            "Un río de aguas negras y lentas bordea las barrancas. "
            "El sonido del agua imita a veces el llanto de un niño. "
            "Algo se mueve bajo la superficie."
        ),
        "exits": {"oeste": "barrancas_entrada"},
        "items": [],
        "creatures": ["ahuizotl"],
        "npcs": [],
        "features": {
            "rio":    "Aguas oscuras. Huelen a petricor y a algo más antiguo.",
            "orilla": "El barro tiene marcas: patas de animal que terminan en dedos humanos.",
        },
    },

    "claro_bosque": {
        "name": "Claro del Bosque",
        "description": (
            "Los árboles se abren en un círculo como si algo los hubiera empujado. "
            "La luz cae más fría aquí. Una figura sentada en una piedra "
            "levanta la vista cuando llegas."
        ),
        "exits": {"sur": "barrancas_entrada", "norte": "ruinas_templo"},
        "items": [],
        "creatures": [],
        "npcs": ["xochitl"],
        "features": {
            "piedra": "Glifos tallados en la piedra donde está Xochitl. Los reconoces: son del Mictlán.",
            "luz":    "Las sombras de Xochitl apuntan en dirección equivocada.",
        },
    },

    "ruinas_templo": {
        "name": "Ruinas del Templo",
        "description": (
            "Muros de piedra volcánica inclinados sin caer — algo los sostiene desde adentro. "
            "Un tzitzimitl patrulla entre los escombros: "
            "esqueleto descarnado adornado con cuchillos de pedernal."
        ),
        "exits": {"sur": "claro_bosque", "norte": "cueva_nahual"},
        "items": [],
        "creatures": ["tzitzimitl"],
        "npcs": [],
        "features": {
            "muros":      "Relieves de estrellas y huesos. Templo para pedir paso seguro en eclipses.",
            "escombros":  "Entre los escombros hay algo enterrado. El tzitzimitl lo vigila.",
        },
    },

    "cueva_nahual": {
        "name": "Cueva del Nahual",
        "description": (
            "La cueva huele a bestia y a obsidiana caliente. "
            "Las paredes brillan con cuarzo negro. "
            "El Nahual de Obsidiana aguarda al fondo: un coyote descarnado del tamaño de un caballo "
            "con costillas de obsidiana que brillan verde enfermo."
        ),
        "exits": {"sur": "ruinas_templo"},
        "locked_exits": {
            "norte": {
                "destination": "portal_mictlan",
                "requires": "obsidiana_bendita",
                "msg": "El portal al norte está sellado con magia antigua. Necesitas la Obsidiana Bendita para abrirlo.",
            }
        },
        "items": ["hierbas_fuertes"],
        "creatures": ["nahual_obsidiana"],
        "npcs": [],
        "features": {
            "paredes":  "Obsidiana en bruto. En las piezas más grandes ves reflejos de cosas que no están aquí.",
            "rastros":  "Arañazos profundos en el suelo. Algo grande, furioso y paciente.",
        },
    },

    "portal_mictlan": {
        "name": "Portal al Mictlán",
        "description": (
            "Un arco de piedra volcánica al fondo de la cueva. "
            "Los bordes vibran con una luz que no es luz — la ausencia ordenada de oscuridad. "
            "A través del arco se ve el primer nivel del Mictlán."
        ),
        "exits": {"sur": "cueva_nahual"},
        "locked_exits": {
            "norte": {
                "destination": "nivel1_orilla",
                "requires": "obsidiana_bendita",
                "msg": "El arco está inactivo. Sostén la Obsidiana Bendita frente a él para activarlo.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "arco": "Los nueve niveles del Mictlán están tallados en el arco. El noveno muestra un trono de cráneos.",
        },
    },

    # ── MICTLÁN — NIVEL 1 ─────────────────────────────────────────────────────
    "nivel1_orilla": {
        "name": "Apanohuaia — Orilla del Chiconahuapan",
        "description": (
            "El río de los muertos. Aguas negras que fluyen en sentido contrario al que deberían. "
            "La orilla está hecha de huesos compactados. "
            "Un Guardián del Río bloquea el único paso al otro lado."
        ),
        "exits": {"sur": "portal_mictlan"},
        "locked_exits": {
            "norte": {
                "destination": "nivel1_cruce",
                "requires_defeated": "guardian_rio",
                "msg": "El Guardián del Río bloquea el paso. Debes derrotarlo o encontrar otra manera.",
            }
        },
        "items": [],
        "creatures": ["guardian_rio"],
        "npcs": [],
        "features": {
            "rio":       "Chiconahuapan. Las aguas del olvido. Sumergirte sin protección borra tu nombre.",
            "orilla":    "Millones de huesos compactados. Cada uno fue una persona.",
            "otro_lado": "La orilla opuesta es oscura y silenciosa. El segundo nivel del Mictlán.",
        },
    },

    "nivel1_cruce": {
        "name": "Apanohuaia — Orilla Opuesta",
        "description": (
            "Has cruzado el primer río del Mictlán. "
            "Detrás de ti el Chiconahuapan sigue fluyendo al revés. "
            "Adelante, la oscuridad se abre hacia el segundo nivel. "
            "Lo que Diego vivió aquí, tú lo estás viviendo ahora."
        ),
        "exits": {"sur": "nivel1_orilla"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "oscuridad": "El segundo nivel. El camino continúa — pero esa es otra historia.",
        },
    },
}

ITEMS = {
    "tlachicotl": {
        "name": "Tlachicotl",
        "description": (
            "Espada de obsidiana volcánica y acero toledano. La hoja absorbe la luz. "
            "Al empuñarla sientes rabia y tristeza que no son tuyas."
        ),
        "type": "weapon",
        "damage": 9,
        "weakness_bonus_vs": "nahual_obsidiana",
    },
    "tonatiuh": {
        "name": "Tonatiuh",
        "description": (
            "Arcabuz con plumas de quetzal y jade. Balas de plata fundida con copal. "
            "Letales para criaturas del inframundo. Quedan pocas — úsalo con sabiduría."
        ),
        "type": "weapon",
        "damage": 13,
        "weakness_bonus_vs": "tzitzimitl",
    },
    "escudo_ceiba": {
        "name": "Escudo Ceiba",
        "description": (
            "Escudo de piel de jaguar sobre madera de ceiba sagrada. "
            "Repele proyectiles y maldiciones. Emite calor al sostenerlo."
        ),
        "type": "shield",
        "damage": 4,
        "defense": 5,
    },
    "copal_sagrado": {
        "name": "Copal Sagrado",
        "description": "Resina consagrada. El humo ahuyenta espíritus y debilita criaturas del inframundo.",
        "type": "ritual",
        "combat_bonus": 6,
        "weakness_bonus_vs": "ahuizotl",
        "use_msg": "Enciendes el copal. El humo sube en espiral y la criatura retrocede, quemada.",
    },
    "caracola_quetzalcoatl": {
        "name": "Caracola de Quetzalcóatl",
        "description": (
            "Su sonido imita el llamado del dios serpiente. "
            "Confunde guardianes que sirven a poderes mayores."
        ),
        "type": "ritual",
        "combat_bonus": 8,
        "weakness_bonus_vs": "guardian_rio",
        "use_msg": "Soplas la caracola. El sonido llena el espacio y la criatura se tambalea, desorientada.",
    },
    "obsidiana_bendita": {
        "name": "Obsidiana Bendita",
        "description": "Fragmento consagrado por ritual. Sella portales y abre caminos entre mundos.",
        "type": "key",
        "use_msg": "La obsidiana brilla al acercarse al portal. El sello se rompe con un sonido de huesos.",
    },
    "tamales_citlali": {
        "name": "Tamales de Citlali",
        "description": "Tamales de frijol y chile en hoja de maíz. Para el camino.",
        "type": "healing",
        "healing": 30,
    },
    "hierbas_curativas": {
        "name": "Hierbas Curativas",
        "description": "Árnica, romero y ruda. Curan heridas menores.",
        "type": "healing",
        "healing": 15,
    },
    "hierbas_fuertes": {
        "name": "Hierbas del Mictlán",
        "description": "Solo crecen cerca de portales al inframundo. Más potentes que cualquier medicina mortal.",
        "type": "healing",
        "healing": 25,
    },
    "fragmento_obsidiana": {
        "name": "Fragmento de Obsidiana",
        "description": "Obsidiana volcánica. Afilado como navaja. Algo en él vibra.",
        "type": "lore",
    },
    "escamas_ahuizotl": {
        "name": "Escamas del Ahuízotl",
        "description": "Escamas duras con reflejo azul-negro. Citlali sabrá para qué sirven.",
        "type": "lore",
    },
}

CREATURES = {
    "ahuizotl": {
        "name": "Ahuízotl",
        "description": (
            "Criatura del tamaño de un perro grande con cuerpo de nutria y "
            "cola que termina en una mano humana. Ojos de obsidiana mojada."
        ),
        "combat_desc": (
            "El Ahuízotl agita su cola-mano. Sus ojos no parpadean. "
            "El llanto que emite suena demasiado humano."
        ),
        "hp": 30,
        "attack": 6,
        "defense": 2,
        "weakness_hint": "El humo sagrado lo quema.",
        "weakness_bonus_vs_item": "copal_sagrado",
        "loot": ["escamas_ahuizotl"],
    },
    "tzitzimitl": {
        "name": "Tzitzimitl",
        "description": (
            "Demonio estelar: esqueleto con cuchillos de pedernal por dedos. "
            "Ata dentro de sí las estrellas que devoró."
        ),
        "combat_desc": (
            "El Tzitzimitl extiende sus brazos-cuchillo. "
            "El aire enfría varios grados. Ataca en ráfagas rápidas."
        ),
        "hp": 40,
        "attack": 8,
        "defense": 3,
        "weakness_hint": "Las balas de plata lo atraviesan.",
        "weakness_bonus_vs_item": "tonatiuh",
        "loot": ["caracola_quetzalcoatl"],
    },
    "nahual_obsidiana": {
        "name": "Nahual de Obsidiana",
        "description": (
            "Coyote descarnado del tamaño de un caballo. "
            "Costillas de obsidiana verde. Su sombra se mueve independiente de su cuerpo."
        ),
        "combat_desc": (
            "El Nahual te rodea con movimientos imposibles. "
            "Su sombra ataca primero, el cuerpo después. "
            "'Hueles a él... al que nos cazaba...' gruñe."
        ),
        "hp": 60,
        "attack": 12,
        "defense": 5,
        "weakness_hint": "La hoja de obsidiana sagrada corta su sombra.",
        "weakness_bonus_vs_item": "tlachicotl",
        "loot": ["obsidiana_bendita"],
    },
    "guardian_rio": {
        "name": "Guardián del Río",
        "description": (
            "Figura de agua negra sin forma definida. "
            "Cuando habla, el sonido llega desde todas las direcciones."
        ),
        "combat_desc": (
            "El Guardián se expande bloqueando el paso. "
            "Voz: '¿Por qué cruzas, vivo?' "
            "La caracola lo desestabiliza."
        ),
        "hp": 35,
        "attack": 7,
        "defense": 4,
        "weakness_hint": "El sonido de la caracola lo confunde.",
        "weakness_bonus_vs_item": "caracola_quetzalcoatl",
        "loot": [],
    },
}

NPCS = {
    "citlali": {
        "name": "Citlali",
        "description": "Anciana curandera. Conoció a Diego antes de que entrara al Mictlán.",
        "dialogue": [
            "Las estrellas sangraron anoche. No es metáfora. "
            "Ve a mi casa — las reliquias de Diego son tuyas. Al este de aquí.",
        ],
        "gives_item": "tamales_citlali",
        "give_msg": "Citlali envuelve tamales en hoja de maíz sin mirarte. 'Para el camino.'",
    },
    "rodrigo": {
        "name": "Capitán Rodrigo",
        "description": "Capitán español con sombras bajo los ojos. Sus hombres desaparecieron en las barrancas.",
        "dialogue": [
            "Mis hombres no vuelven del río al este de las barrancas. "
            "Algo los atrae. Cuídate del agua oscura.",
        ],
        "gives_item": None,
    },
    "vendedora": {
        "name": "Doña Esperanza",
        "description": "Vendedora del mercado. Lleva décadas aquí y ha visto de todo.",
        "dialogue": [
            "Las hierbas del mostrador son tuyas, tómalas. "
            "El copal fuerte está en casa de Citlali — ese es el que sirve contra criaturas.",
        ],
        "gives_item": None,
    },
    "xochitl": {
        "name": "Xochitl",
        "description": "Espíritu de una joven que murió hace treinta años. Lleva ropa de esa época.",
        "dialogue": [
            "Diego me prometió que alguien vendría. Eres tú. "
            "El Nahual está en la cueva al norte del templo. Necesitas Tlachicotl para herirlo de verdad. "
            "Y para entrar al Mictlán necesitas lo que él guarda.",
        ],
        "gives_item": None,
    },
}
