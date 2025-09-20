---
id: Ultrasonicexcalidraw
aliases: []
tags: [excalidraw]
excalidraw-plugin: parsed
dg-publish: true
---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==

# Text Elements
- Power Supply	5V DC
- Working Current	15 mA
- Working Frequency	40 kHz
- Maximum Range	4 meters
- Minimum Range	2 cm
 - Measuring Angle	15º
- Resolution	0.3 cm
- Trigger Input Signal	10uS TTL pulse
- Echo Output Signal	TTL pulse proportional to the distance range
- Dimensions	45mm x 20mm x 15mm

 ^Rm48ezvl

VCC	Powers the sensor (5V)
Trig	Trigger Input Pin
Echo	Echo Output Pin
GND	Common GND ^gbWLs0nt

ESP
8266
 ^w5yshfdl

# Element Links
OC8ZL8jD: [[Ultrasonic Sensor Code]]

# Embedded files
6bccad5f9ba762c9bc08befd033bdbbf5ccf57e4: $$Distance = \frac{Speed \ of \ light  \ in \ air  \times time}{2}
$$
ef98c6fda17fe8ab795a4cecaf82d33f9f04d948: https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2021/06/ESP8266-Ultrasonic-Sensor-Wiring-Fritzing-Diagram.png?w=738&quality=100&strip=all&ssl=1
cde82f2c73f7bbdcabe70313928de75a6d9f1cec: https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2021/06/how-ultrasonic-sensor-works-01.png?w=750&quality=100&strip=all&ssl=1
02e27d046075b40807129a36eec75f02cf77f221: https://www.teachmemicro.com/wp-content/uploads/2018/04/NodeMCUv3.0-pinout.jpg

%%
# Drawing

```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.1.6",
	"elements": [
		{
			"type": "image",
			"version": 55,
			"versionNonce": 1795033716,
			"isDeleted": false,
			"id": "hdWYHCnm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 93.12941196986628,
			"y": -188.88612932536762,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 500,
			"height": 397.69647696476966,
			"seed": 70384,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ef98c6fda17fe8ab795a4cecaf82d33f9f04d948",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 147,
			"versionNonce": 1402275532,
			"isDeleted": false,
			"id": "feFhdzPg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 115.04184722413004,
			"y": 569.316120137395,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 500,
			"height": 302,
			"seed": 76242,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "cde82f2c73f7bbdcabe70313928de75a6d9f1cec",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 101,
			"versionNonce": 557620212,
			"isDeleted": false,
			"id": "Rm48ezvl",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -611.4520033161991,
			"y": -193.23094722163663,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 741.419189453125,
			"height": 300,
			"seed": 1351852693,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "- Power Supply\t5V DC\n- Working Current\t15 mA\n- Working Frequency\t40 kHz\n- Maximum Range\t4 meters\n- Minimum Range\t2 cm\n - Measuring Angle\t15º\n- Resolution\t0.3 cm\n- Trigger Input Signal\t10uS TTL pulse\n- Echo Output Signal\tTTL pulse proportional to the distance range\n- Dimensions\t45mm x 20mm x 15mm\n\n",
			"rawText": "- Power Supply\t5V DC\n- Working Current\t15 mA\n- Working Frequency\t40 kHz\n- Maximum Range\t4 meters\n- Minimum Range\t2 cm\n - Measuring Angle\t15º\n- Resolution\t0.3 cm\n- Trigger Input Signal\t10uS TTL pulse\n- Echo Output Signal\tTTL pulse proportional to the distance range\n- Dimensions\t45mm x 20mm x 15mm\n\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "- Power Supply\t5V DC\n- Working Current\t15 mA\n- Working Frequency\t40 kHz\n- Maximum Range\t4 meters\n- Minimum Range\t2 cm\n - Measuring Angle\t15º\n- Resolution\t0.3 cm\n- Trigger Input Signal\t10uS TTL pulse\n- Echo Output Signal\tTTL pulse proportional to the distance range\n- Dimensions\t45mm x 20mm x 15mm\n\n",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 129,
			"versionNonce": 325209420,
			"isDeleted": false,
			"id": "gbWLs0nt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -596.489773905392,
			"y": 86.75011060756088,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 344.53961181640625,
			"height": 100,
			"seed": 60811,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "VCC\tPowers the sensor (5V)\nTrig\tTrigger Input Pin\nEcho\tEcho Output Pin\nGND\tCommon GND",
			"rawText": "VCC\tPowers the sensor (5V)\nTrig\tTrigger Input Pin\nEcho\tEcho Output Pin\nGND\tCommon GND",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "VCC\tPowers the sensor (5V)\nTrig\tTrigger Input Pin\nEcho\tEcho Output Pin\nGND\tCommon GND",
			"lineHeight": 1.25
		},
		{
			"type": "image",
			"version": 79,
			"versionNonce": 78445940,
			"isDeleted": false,
			"id": "01TzQuJa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -584.095303690548,
			"y": 268.5707588009203,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 350,
			"height": 40,
			"seed": 79425,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "6bccad5f9ba762c9bc08befd033bdbbf5ccf57e4",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "embeddable",
			"version": 110,
			"versionNonce": 650298316,
			"isDeleted": false,
			"id": "OC8ZL8jD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -624.2684938528434,
			"y": 371.67081752732315,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 702.353006998698,
			"height": 522.821756998698,
			"seed": 9390,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": "[[Ultrasonic Sensor Code]]",
			"locked": false,
			"customData": {
				"mdProps": {
					"useObsidianDefaults": false,
					"backgroundMatchCanvas": false,
					"backgroundMatchElement": true,
					"backgroundColor": "#fff",
					"backgroundOpacity": 60,
					"borderMatchElement": true,
					"borderColor": "#fff",
					"borderOpacity": 0,
					"filenameVisible": false
				}
			},
			"scale": [
				1,
				1
			]
		},
		{
			"type": "line",
			"version": 150,
			"versionNonce": 781528820,
			"isDeleted": false,
			"id": "sMKhXFB8CQnB72z6bKs0Z",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -126.48150380939865,
			"y": 1463.2730257866929,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 304.75839468149036,
			"height": 439.58251953125,
			"seed": 1140643060,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-4.2132568359375,
					428.34716796875
				],
				[
					299.1407658503605,
					422.7294921875
				],
				[
					300.54513784555286,
					-11.2353515625
				]
			]
		},
		{
			"type": "freedraw",
			"version": 83,
			"versionNonce": 332425804,
			"isDeleted": false,
			"id": "Mygs0pHcwOgADLmysy17I",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 115.07813223326957,
			"y": 1373.3904010871738,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 195.2139047475962,
			"height": 88.4782527043269,
			"seed": 1151683660,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.404371995192264,
					-1.4044658954328497
				],
				[
					-8.426513671875,
					0
				],
				[
					-14.044095552884642,
					2.808837890625
				],
				[
					-23.875075120192264,
					7.02204777644215
				],
				[
					-32.301588792067264,
					9.83088566706715
				],
				[
					-42.13247445913464,
					15.44856144831715
				],
				[
					-51.963360126201906,
					19.661771334134528
				],
				[
					-56.17666391225964,
					21.06623722956715
				],
				[
					-64.6031306340144,
					25.279447115384528
				],
				[
					-67.4119685246394,
					26.68391301081715
				],
				[
					-68.8163874699519,
					26.68391301081715
				],
				[
					-75.8384821965144,
					29.49275090144215
				],
				[
					-77.2429011418269,
					30.897122896634528
				],
				[
					-78.6473200871394,
					32.30158879206715
				],
				[
					-81.4561579777644,
					33.70596078725953
				],
				[
					-82.8605769230769,
					35.11042668269215
				],
				[
					-84.2649958683894,
					37.91926457331715
				],
				[
					-84.2649958683894,
					40.72810246394215
				],
				[
					-85.6694148137019,
					46.345684344951906
				],
				[
					-85.6694148137019,
					49.154522235576906
				],
				[
					-85.6694148137019,
					51.963360126201906
				],
				[
					-84.2649958683894,
					57.581035907451906
				],
				[
					-84.2649958683894,
					61.79433969350953
				],
				[
					-82.8605769230769,
					61.79433969350953
				],
				[
					-78.6473200871394,
					64.60317758413453
				],
				[
					-75.8384821965144,
					66.0075495793269
				],
				[
					-71.6252253605769,
					66.0075495793269
				],
				[
					-67.4119685246394,
					67.41201547475953
				],
				[
					-63.198711688701906,
					67.41201547475953
				],
				[
					-54.772198016826906,
					67.41201547475953
				],
				[
					-51.963360126201906,
					67.41201547475953
				],
				[
					-44.94131234975964,
					67.41201547475953
				],
				[
					-29.492750901442264,
					68.8163874699519
				],
				[
					-4.213209885817264,
					74.4340632512019
				],
				[
					12.639817457932736,
					77.2429011418269
				],
				[
					50.55898813100964,
					82.8605769230769
				],
				[
					57.581129807692264,
					84.26494891826906
				],
				[
					61.79433969350964,
					84.26494891826906
				],
				[
					77.24299504206726,
					87.07378680889406
				],
				[
					81.45620492788464,
					87.07378680889406
				],
				[
					88.4782527043269,
					87.07378680889406
				],
				[
					95.50039438100964,
					85.6694148137019
				],
				[
					99.7136042668269,
					82.8605769230769
				],
				[
					103.92690805288464,
					80.0517390324519
				],
				[
					106.73574594350964,
					77.2429011418269
				],
				[
					109.54448993389428,
					73.02959735576906
				],
				[
					109.54448993389428,
					68.8163874699519
				],
				[
					109.54448993389428,
					66.0075495793269
				],
				[
					109.54448993389428,
					60.389873798076906
				],
				[
					108.1401179387019,
					50.55898813100953
				],
				[
					106.73574594350964,
					47.75015024038453
				],
				[
					103.92690805288464,
					42.13247445913453
				],
				[
					99.7136042668269,
					37.91926457331715
				],
				[
					94.0959284855769,
					35.11042668269215
				],
				[
					89.88271859975964,
					32.30158879206715
				],
				[
					81.45620492788464,
					28.088285006009528
				],
				[
					78.64736703725964,
					26.68391301081715
				],
				[
					68.81648137019226,
					23.87507512019215
				],
				[
					53.36782602163464,
					16.852933443509528
				],
				[
					44.94140625,
					14.044095552884528
				],
				[
					36.514892578125,
					11.2353515625
				],
				[
					29.492750901442264,
					9.83088566706715
				],
				[
					19.661865234375,
					8.426513671875
				],
				[
					15.448655348557736,
					8.426513671875
				],
				[
					8.426513671875,
					8.426513671875
				],
				[
					1.404465895432736,
					8.426513671875
				],
				[
					-8.426513671875,
					8.426513671875
				],
				[
					-14.044095552884642,
					8.426513671875
				],
				[
					-16.85293344350964,
					8.426513671875
				],
				[
					-25.27944711538464,
					8.426513671875
				],
				[
					-29.492750901442264,
					8.426513671875
				],
				[
					-42.13247445913464,
					12.63972355769215
				],
				[
					-43.536846454326906,
					14.044095552884528
				],
				[
					-43.536846454326906,
					14.044095552884528
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 30,
			"versionNonce": 528167028,
			"isDeleted": false,
			"id": "PyntvRi2BIFWx-rtQmSLT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 193.7254992705292,
			"y": 1393.0521724213083,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 113.7577937199519,
			"height": 2.808837890625,
			"seed": 2052217420,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					46.345778245192264,
					-2.808837890625
				],
				[
					50.55898813100964,
					-2.808837890625
				],
				[
					53.36782602163464,
					-2.808837890625
				],
				[
					54.772291917067264,
					-2.808837890625
				],
				[
					56.17666391225964,
					-2.808837890625
				],
				[
					58.98550180288464,
					-2.808837890625
				],
				[
					63.198711688701906,
					-2.808837890625
				],
				[
					66.0075495793269,
					-2.808837890625
				],
				[
					70.22085336538464,
					-2.808837890625
				],
				[
					74.4340632512019,
					-2.808837890625
				],
				[
					77.2429011418269,
					-2.808837890625
				],
				[
					81.45620492788464,
					-2.808837890625
				],
				[
					87.07388070913464,
					-2.808837890625
				],
				[
					91.2870905949519,
					-2.808837890625
				],
				[
					98.30913837139417,
					-2.808837890625
				],
				[
					101.11797626201917,
					-2.808837890625
				],
				[
					102.5224421574519,
					-2.808837890625
				],
				[
					106.73565204326917,
					-2.808837890625
				],
				[
					109.54448993389417,
					-2.808837890625
				],
				[
					113.7577937199519,
					-2.808837890625
				],
				[
					113.7577937199519,
					-2.808837890625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 28,
			"versionNonce": 224739532,
			"isDeleted": false,
			"id": "_C53-a5ItS8aYBLE5rXpc",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 226.02708806259648,
			"y": 1442.2067885571257,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 81.45620492788464,
			"height": 7.022047776442378,
			"seed": 1477054412,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					37.91926457331738,
					-7.022047776442378
				],
				[
					42.13247445913464,
					-7.022047776442378
				],
				[
					43.53694035456738,
					-7.022047776442378
				],
				[
					49.15461613581738,
					-7.022047776442378
				],
				[
					50.55898813100964,
					-7.022047776442378
				],
				[
					56.17666391225964,
					-7.022047776442378
				],
				[
					58.98550180288464,
					-7.022047776442378
				],
				[
					60.389873798076906,
					-7.022047776442378
				],
				[
					63.198711688701906,
					-7.022047776442378
				],
				[
					66.0075495793269,
					-7.022047776442378
				],
				[
					68.8163874699519,
					-7.022047776442378
				],
				[
					70.22085336538464,
					-7.022047776442378
				],
				[
					73.02969125600964,
					-7.022047776442378
				],
				[
					74.4340632512019,
					-5.61767578125
				],
				[
					75.83852914663464,
					-5.61767578125
				],
				[
					77.2429011418269,
					-5.61767578125
				],
				[
					78.64736703725964,
					-4.213209885817378
				],
				[
					81.45620492788464,
					-2.808837890625
				],
				[
					81.45620492788464,
					-2.808837890625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "rectangle",
			"version": 34,
			"versionNonce": 1462043124,
			"isDeleted": false,
			"id": "1eMvppdZ7ukbCJB1cT8MI",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 381.91735624168314,
			"y": 1492.7657766881352,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 137.63286884014406,
			"height": 241.55968299278834,
			"seed": 1522178124,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "w5yshfdl"
				}
			],
			"updated": 1715072128215,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 19,
			"versionNonce": 1528514380,
			"isDeleted": false,
			"id": "w5yshfdl",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 423.16381385511454,
			"y": 1576.0456181845293,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 55.13995361328125,
			"height": 75,
			"seed": 1666018036,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128215,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "ESP\n8266\n",
			"rawText": "ESP\n8266\n",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "1eMvppdZ7ukbCJB1cT8MI",
			"originalText": "ESP\n8266\n",
			"lineHeight": 1.25
		},
		{
			"type": "ellipse",
			"version": 21,
			"versionNonce": 1821942644,
			"isDeleted": false,
			"id": "pdpipAqxPJKiyFdzuu8o9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 270.00745006284956,
			"y": 1851.8529381214153,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 29.492750901442264,
			"height": 33.7060546875,
			"seed": 686518260,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 28,
			"versionNonce": 1095531980,
			"isDeleted": false,
			"id": "AguKQ6nJlyxjGFVjKXssC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 345.2824838669362,
			"y": 1854.528215275388,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 29.492750901442264,
			"height": 33.7060546875,
			"seed": 1966208628,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 34,
			"versionNonce": 639374580,
			"isDeleted": false,
			"id": "hPT7DUXVYpAgy1OKLK-u0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 410.2912314156456,
			"y": 1853.3682310110917,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 29.492750901442264,
			"height": 33.7060546875,
			"seed": 1809181044,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 51,
			"versionNonce": 1762845772,
			"isDeleted": false,
			"id": "wSO5ggfWgXFapai7x0KL6",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 470.7044418945171,
			"y": 1854.1349808371288,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 29.492750901442264,
			"height": 33.7060546875,
			"seed": 1784224884,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false
		},
		{
			"type": "freedraw",
			"version": 36,
			"versionNonce": 288708212,
			"isDeleted": false,
			"id": "zbQ-dLxG2dZS8_StyWReZ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 276.8038654458836,
			"y": 1888.7978311910447,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 2.8827225534539593,
			"height": 46.123946340460634,
			"seed": 1641483508,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.960886101973756,
					1.921772203947512
				],
				[
					0.960886101973756,
					3.843672902960634
				],
				[
					0.960886101973756,
					5.765445106907919
				],
				[
					0.960886101973756,
					7.687217310855431
				],
				[
					0.960886101973756,
					11.530890213815837
				],
				[
					0.960886101973756,
					13.45279091282896
				],
				[
					0.960886101973756,
					14.413677014802715
				],
				[
					0.960886101973756,
					17.296463815789593
				],
				[
					0.960886101973756,
					18.257349917763122
				],
				[
					0.960886101973756,
					21.14013671875
				],
				[
					0.960886101973756,
					23.061908922697512
				],
				[
					0.960886101973756,
					24.022923519736878
				],
				[
					0.960886101973756,
					25.944695723684163
				],
				[
					0.960886101973756,
					26.90558182565792
				],
				[
					0.960886101973756,
					27.866467927631675
				],
				[
					0.960886101973756,
					28.82748252467104
				],
				[
					0.960886101973756,
					30.749254728618553
				],
				[
					0.960886101973756,
					31.71014083059208
				],
				[
					0,
					34.59292763157896
				],
				[
					0,
					35.553813733552715
				],
				[
					-0.9608861019736423,
					37.47571443256584
				],
				[
					-0.9608861019736423,
					39.39748663651312
				],
				[
					-0.9608861019736423,
					40.358501233552715
				],
				[
					-0.9608861019736423,
					41.31938733552647
				],
				[
					-0.9608861019736423,
					42.2802734375
				],
				[
					-0.9608861019736423,
					43.241159539473756
				],
				[
					-0.9608861019736423,
					44.20217413651312
				],
				[
					-0.9608861019736423,
					45.16306023848688
				],
				[
					-0.9608861019736423,
					46.123946340460634
				],
				[
					-1.9218364514802033,
					46.123946340460634
				],
				[
					-1.9218364514802033,
					46.123946340460634
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1212709580,
			"isDeleted": false,
			"id": "n_6OJwG2grLGxlHEQ_yu8",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 253.7418922756534,
			"y": 1935.8826636334788,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 53.81129214638156,
			"height": 0.960886101973756,
			"seed": 592871028,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9608861019736423,
					0
				],
				[
					7.687281558388122,
					0
				],
				[
					17.29646381578948,
					0
				],
				[
					35.55387798108552,
					0
				],
				[
					46.12394634046052,
					0
				],
				[
					53.81129214638156,
					0
				],
				[
					52.850406044407805,
					0.960886101973756
				],
				[
					52.850406044407805,
					0.960886101973756
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 447375348,
			"isDeleted": false,
			"id": "bkBvJrxs5Ig2sCJ7Z3wvH",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 262.3901241835481,
			"y": 1945.4919101384132,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 25.94475997121708,
			"height": 0,
			"seed": 2023275892,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					24.022923519736878,
					0
				],
				[
					24.98380962171052,
					0
				],
				[
					25.94475997121708,
					0
				],
				[
					25.94475997121708,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 159859020,
			"isDeleted": false,
			"id": "39YHhDN-kQKClH2mJL0eI",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 268.15563353798893,
			"y": 1953.1792559443343,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 9.609118009868439,
			"height": 0,
			"seed": 290526836,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					9.609118009868439,
					0
				],
				[
					9.609118009868439,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 24,
			"versionNonce": 646007156,
			"isDeleted": false,
			"id": "KDR_INXECimAw39VHMstw",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 350.79447245657445,
			"y": 1886.8759304920316,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 4.804623252467195,
			"height": 55.7331928453948,
			"seed": 1843936372,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.8436729029605203,
					16.335577713815837
				],
				[
					3.8436729029605203,
					20.179250616776244
				],
				[
					3.8436729029605203,
					24.022923519736878
				],
				[
					3.8436729029605203,
					26.905710320723756
				],
				[
					3.8436729029605203,
					29.788368626644797
				],
				[
					3.8436729029605203,
					31.71026932565792
				],
				[
					3.8436729029605203,
					32.671155427631675
				],
				[
					3.8436729029605203,
					37.47571443256584
				],
				[
					3.8436729029605203,
					39.39761513157896
				],
				[
					2.8827225534538456,
					42.28040193256584
				],
				[
					2.8827225534538456,
					44.20217413651312
				],
				[
					2.8827225534538456,
					45.16306023848688
				],
				[
					2.8827225534538456,
					48.045847039473756
				],
				[
					1.9218364514802033,
					50.928633840460634
				],
				[
					1.9218364514802033,
					51.88951994243416
				],
				[
					1.9218364514802033,
					52.85040604440792
				],
				[
					0,
					55.7331928453948
				],
				[
					-0.9609503495066747,
					55.7331928453948
				],
				[
					-0.9609503495066747,
					55.7331928453948
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 19,
			"versionNonce": 1948858316,
			"isDeleted": false,
			"id": "nojesIicPxOsS98YHEHVL",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 336.38073119423893,
			"y": 1951.257355245321,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 37.475714432565724,
			"height": 0.9608861019735286,
			"seed": 420449268,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					6.726395456414366,
					0
				],
				[
					10.570068359375,
					0
				],
				[
					14.41374126233552,
					0
				],
				[
					18.25741416529604,
					0
				],
				[
					24.022859272203846,
					-0.9608861019735286
				],
				[
					24.98380962171052,
					-0.9608861019735286
				],
				[
					26.905646073190724,
					-0.9608861019735286
				],
				[
					29.788368626644683,
					-0.9608861019735286
				],
				[
					33.6320415296052,
					-0.9608861019735286
				],
				[
					34.592991879111764,
					-0.9608861019735286
				],
				[
					35.55387798108541,
					-0.9608861019735286
				],
				[
					36.51482833059208,
					-0.9608861019735286
				],
				[
					37.475714432565724,
					-0.9608861019735286
				],
				[
					37.475714432565724,
					-0.9608861019735286
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 671087348,
			"isDeleted": false,
			"id": "Iyw6pePcp5goSHv8TwTyA",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 343.1071266506533,
			"y": 1958.9447010512422,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 33.632105777138236,
			"height": 0.960886101973756,
			"seed": 746529780,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					29.788432874177715,
					-0.960886101973756
				],
				[
					31.71026932565792,
					-0.960886101973756
				],
				[
					33.632105777138236,
					-0.960886101973756
				],
				[
					32.671155427631675,
					-0.960886101973756
				],
				[
					32.671155427631675,
					-0.960886101973756
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1414028876,
			"isDeleted": false,
			"id": "CZi4LjNS-34R3KjmkwkD8",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 351.7553585585481,
			"y": 1965.6711607551895,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 11.531018708881561,
			"height": 0,
			"seed": 1646321268,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					11.531018708881561,
					0
				],
				[
					11.531018708881561,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 967605364,
			"isDeleted": false,
			"id": "maM5THNjLRS8y7bNHOjLv",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 347.9116856555876,
			"y": 1930.1172185265712,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 3.8436729029605203,
			"height": 19.218364514802488,
			"seed": 345244788,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.8436729029605203,
					14.413677014802488
				],
				[
					3.8436729029605203,
					15.374691611842081
				],
				[
					3.8436729029605203,
					17.296463815789366
				],
				[
					3.8436729029605203,
					19.218364514802488
				],
				[
					3.8436729029605203,
					19.218364514802488
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 1656665292,
			"isDeleted": false,
			"id": "m1AplPaspROTN5Zlo8jKg",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 423.8241291177586,
			"y": 1888.7978311910447,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 0.9608861019736423,
			"height": 58.61585115131584,
			"seed": 1292848884,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					36.51482833059208
				],
				[
					0,
					37.47571443256584
				],
				[
					0,
					40.358501233552715
				],
				[
					0,
					42.2802734375
				],
				[
					0,
					45.16306023848688
				],
				[
					0,
					48.04571854440792
				],
				[
					0,
					49.00673314144751
				],
				[
					0,
					49.96761924342104
				],
				[
					0,
					54.7721782483552
				],
				[
					0.9608861019736423,
					56.69407894736855
				],
				[
					0.9608861019736423,
					57.65496504934208
				],
				[
					0,
					58.61585115131584
				],
				[
					0,
					58.61585115131584
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 8,
			"versionNonce": 894225908,
			"isDeleted": false,
			"id": "hpe5FyvPn28WWUnI9dmqz",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 392.1138597921007,
			"y": 1940.6872226384132,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 47.0849609375,
			"height": 1.921772203947512,
			"seed": 1363654004,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					47.0849609375,
					-1.921772203947512
				],
				[
					45.16312448601968,
					-0.960886101973756
				],
				[
					45.16312448601968,
					-0.960886101973756
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 757480268,
			"isDeleted": false,
			"id": "BdklJzRhswPKDnIZKyI1r",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 409.4103878554231,
			"y": 1947.4136823423605,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 21.14013671875,
			"height": 3.843672902960634,
			"seed": 587451636,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					21.14013671875,
					-3.843672902960634
				],
				[
					21.14013671875,
					-3.843672902960634
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1273425780,
			"isDeleted": false,
			"id": "I4zBEh7MdZ5qPKO-HFzPg",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 418.0586197633178,
			"y": 1953.1792559443343,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 13.452855160361878,
			"height": 1.9219006990133494,
			"seed": 2001449716,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					13.452855160361878,
					-1.9219006990133494
				],
				[
					13.452855160361878,
					-1.9219006990133494
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 2111369676,
			"isDeleted": false,
			"id": "EYaJ-nt6Pl075_J1qbtJM",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 417.09773366134414,
			"y": 1961.8274878522288,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 12.491904810855203,
			"height": 0.961014597039366,
			"seed": 1836095732,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					12.491904810855203,
					-0.961014597039366
				],
				[
					12.491904810855203,
					-0.961014597039366
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 499179764,
			"isDeleted": false,
			"id": "hVSHlDYEY0kKmX-of9k8g",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 476.6745351621664,
			"y": 1884.9541582880843,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 4.804623252467195,
			"height": 59.576737253289366,
			"seed": 787644148,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.882786800986878,
					41.319387335526244
				],
				[
					2.882786800986878,
					45.16306023848688
				],
				[
					4.804623252467195,
					52.85040604440792
				],
				[
					4.804623252467195,
					54.7721782483552
				],
				[
					4.804623252467195,
					55.73306435032896
				],
				[
					4.804623252467195,
					58.61585115131561
				],
				[
					3.8436729029605203,
					59.576737253289366
				],
				[
					3.8436729029605203,
					59.576737253289366
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1139857484,
			"isDeleted": false,
			"id": "XoCHN_cRT4EhzAZYqukzB",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 461.29990779785726,
			"y": 1946.4527962403868,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 44.2021098889802,
			"height": 3.8436729029604066,
			"seed": 1078337012,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					44.2021098889802,
					-3.8436729029604066
				],
				[
					44.2021098889802,
					-3.8436729029604066
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1382064756,
			"isDeleted": false,
			"id": "wKY6_lZTCugRZ3i0VCJRs",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 470.9090258077257,
			"y": 1955.1010281482816,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 12.491904810855203,
			"height": 2.882786800986878,
			"seed": 207455220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					12.491904810855203,
					-2.882786800986878
				],
				[
					12.491904810855203,
					-2.882786800986878
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 8,
			"versionNonce": 2068311756,
			"isDeleted": false,
			"id": "x8BWbu8Um9HrOzRaRRTVZ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 477.6354855116731,
			"y": 1965.6711607551895,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 11.530954461348642,
			"height": 0.9610145970395934,
			"seed": 1452403188,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128216,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					10.570068359375,
					0
				],
				[
					11.530954461348642,
					-0.9610145970395934
				],
				[
					11.530954461348642,
					-0.9610145970395934
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 169,
			"versionNonce": 814494708,
			"isDeleted": false,
			"id": "jbyyMnImd-634IDaCOk5y",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 524.7203822016402,
			"y": 1680.2788653193343,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 69.18604800575656,
			"height": 221.97175678453937,
			"seed": 302651380,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9608861019736423,
					0
				],
				[
					4.804559004934163,
					0.960886101973756
				],
				[
					6.72639545641448,
					1.9218364514804307
				],
				[
					8.648231907894683,
					2.8827225534539593
				],
				[
					11.531018708881561,
					2.8827225534539593
				],
				[
					13.452855160361764,
					3.8436729029604066
				],
				[
					14.41374126233552,
					3.8436729029604066
				],
				[
					15.374691611842081,
					4.804559004934163
				],
				[
					15.374691611842081,
					5.765509354440837
				],
				[
					16.335577713815724,
					8.64823190789457
				],
				[
					16.335577713815724,
					12.49190481085543
				],
				[
					18.25741416529604,
					22.101087068256675
				],
				[
					20.179250616776244,
					32.671155427631675
				],
				[
					22.10108706825656,
					43.241223787006675
				],
				[
					24.022923519736764,
					50.92856959292749
				],
				[
					24.98380962171052,
					63.42053865131584
				],
				[
					24.98380962171052,
					66.30319695723688
				],
				[
					24.98380962171052,
					73.99054276315792
				],
				[
					24.98380962171052,
					79.75611636513167
				],
				[
					24.98380962171052,
					93.2089072779604
				],
				[
					24.98380962171052,
					95.13067948190792
				],
				[
					24.98380962171052,
					101.8571391858552
				],
				[
					24.98380962171052,
					102.81802528782896
				],
				[
					24.98380962171052,
					105.70081208881584
				],
				[
					24.98380962171052,
					106.66169819078937
				],
				[
					24.022923519736764,
					109.54448499177624
				],
				[
					24.022923519736764,
					112.42727179276312
				],
				[
					24.022923519736764,
					113.38815789473688
				],
				[
					23.061973170230203,
					114.3490439967104
				],
				[
					23.061973170230203,
					115.30993009868416
				],
				[
					22.10108706825656,
					117.23183079769728
				],
				[
					21.14013671875,
					117.23183079769728
				],
				[
					20.179250616776244,
					117.23183079769728
				],
				[
					19.2183645148026,
					117.23183079769728
				],
				[
					18.25741416529604,
					117.23183079769728
				],
				[
					16.335577713815724,
					118.19271689967104
				],
				[
					15.374691611842081,
					119.1536030016448
				],
				[
					13.452855160361764,
					120.11461759868416
				],
				[
					11.531018708881561,
					121.07550370065792
				],
				[
					12.491904810855203,
					121.07550370065792
				],
				[
					14.41374126233552,
					121.07550370065792
				],
				[
					16.335577713815724,
					122.03638980263145
				],
				[
					17.296528063322285,
					122.03638980263145
				],
				[
					20.179250616776244,
					122.03638980263145
				],
				[
					21.14013671875,
					122.03638980263145
				],
				[
					22.10108706825656,
					122.03638980263145
				],
				[
					22.10108706825656,
					122.9972759046052
				],
				[
					23.061973170230203,
					123.9582905016448
				],
				[
					23.061973170230203,
					124.91917660361833
				],
				[
					22.10108706825656,
					125.88006270559208
				],
				[
					21.14013671875,
					126.84094880756584
				],
				[
					19.2183645148026,
					126.84094880756584
				],
				[
					18.25741416529604,
					126.84094880756584
				],
				[
					16.335577713815724,
					127.8019634046052
				],
				[
					14.41374126233552,
					128.76284950657896
				],
				[
					13.452855160361764,
					128.76284950657896
				],
				[
					13.452855160361764,
					129.7237356085525
				],
				[
					12.491904810855203,
					130.68462171052624
				],
				[
					10.570068359375,
					131.64563630756584
				],
				[
					9.609182257401244,
					131.64563630756584
				],
				[
					8.648231907894683,
					131.64563630756584
				],
				[
					9.609182257401244,
					132.60652240953937
				],
				[
					10.570068359375,
					132.60652240953937
				],
				[
					13.452855160361764,
					132.60652240953937
				],
				[
					22.10108706825656,
					132.60652240953937
				],
				[
					24.022923519736764,
					132.60652240953937
				],
				[
					24.98380962171052,
					132.60652240953937
				],
				[
					25.94475997121708,
					132.60652240953937
				],
				[
					26.905646073190724,
					132.60652240953937
				],
				[
					25.94475997121708,
					134.52829461348688
				],
				[
					24.98380962171052,
					134.52829461348688
				],
				[
					23.061973170230203,
					135.4891807154604
				],
				[
					20.179250616776244,
					137.41108141447376
				],
				[
					18.25741416529604,
					138.37196751644728
				],
				[
					16.335577713815724,
					139.33285361842104
				],
				[
					15.374691611842081,
					139.33285361842104
				],
				[
					13.452855160361764,
					140.2938682154604
				],
				[
					12.491904810855203,
					141.25475431743416
				],
				[
					11.531018708881561,
					141.25475431743416
				],
				[
					11.531018708881561,
					142.21564041940792
				],
				[
					12.491904810855203,
					142.21564041940792
				],
				[
					14.41374126233552,
					142.21564041940792
				],
				[
					17.296528063322285,
					143.17652652138145
				],
				[
					19.2183645148026,
					143.17652652138145
				],
				[
					21.14013671875,
					143.17652652138145
				],
				[
					23.061973170230203,
					143.17652652138145
				],
				[
					24.022923519736764,
					143.17652652138145
				],
				[
					24.98380962171052,
					143.17652652138145
				],
				[
					27.866596422697285,
					143.17652652138145
				],
				[
					29.7884328741776,
					143.17652652138145
				],
				[
					30.749318976151244,
					143.17652652138145
				],
				[
					31.710269325657805,
					143.17652652138145
				],
				[
					33.63210577713812,
					143.17652652138145
				],
				[
					32.67115542763156,
					143.17652652138145
				],
				[
					28.82748252467104,
					144.13754111842104
				],
				[
					24.022923519736764,
					147.02019942434208
				],
				[
					23.061973170230203,
					147.02019942434208
				],
				[
					20.179250616776244,
					147.98121402138145
				],
				[
					18.25741416529604,
					148.9421001233552
				],
				[
					14.41374126233552,
					149.90298622532896
				],
				[
					10.570068359375,
					151.82488692434208
				],
				[
					8.648231907894683,
					152.78577302631584
				],
				[
					9.609182257401244,
					152.78577302631584
				],
				[
					10.570068359375,
					152.78577302631584
				],
				[
					12.491904810855203,
					152.78577302631584
				],
				[
					13.452855160361764,
					153.74665912828937
				],
				[
					14.41374126233552,
					153.74665912828937
				],
				[
					15.374691611842081,
					154.70754523026312
				],
				[
					16.335577713815724,
					155.66843133223688
				],
				[
					17.296528063322285,
					156.62944592927624
				],
				[
					18.25741416529604,
					156.62944592927624
				],
				[
					19.2183645148026,
					156.62944592927624
				],
				[
					19.2183645148026,
					157.59033203125
				],
				[
					19.2183645148026,
					159.51210423519728
				],
				[
					19.2183645148026,
					162.39489103618416
				],
				[
					19.2183645148026,
					165.27767783717104
				],
				[
					19.2183645148026,
					170.0822368421052
				],
				[
					19.2183645148026,
					172.96502364309208
				],
				[
					19.2183645148026,
					174.88679584703937
				],
				[
					19.2183645148026,
					178.73046875
				],
				[
					19.2183645148026,
					180.65236944901312
				],
				[
					19.2183645148026,
					184.49604235197353
				],
				[
					19.2183645148026,
					186.41781455592104
				],
				[
					19.2183645148026,
					188.33971525493416
				],
				[
					19.2183645148026,
					192.18338815789457
				],
				[
					19.2183645148026,
					193.14427425986833
				],
				[
					19.2183645148026,
					196.98794716282896
				],
				[
					19.2183645148026,
					197.9488332648025
				],
				[
					19.2183645148026,
					198.90971936677624
				],
				[
					19.2183645148026,
					201.79250616776312
				],
				[
					19.2183645148026,
					204.67529296875
				],
				[
					19.2183645148026,
					206.59706517269728
				],
				[
					19.2183645148026,
					207.55795127467104
				],
				[
					19.2183645148026,
					208.5189658717104
				],
				[
					19.2183645148026,
					212.36263877467104
				],
				[
					19.2183645148026,
					214.28441097861833
				],
				[
					19.2183645148026,
					215.24529708059208
				],
				[
					17.296528063322285,
					217.1671977796052
				],
				[
					16.335577713815724,
					218.12808388157896
				],
				[
					15.374691611842081,
					218.12808388157896
				],
				[
					13.452855160361764,
					219.0889699835525
				],
				[
					12.491904810855203,
					220.04985608552624
				],
				[
					11.531018708881561,
					220.04985608552624
				],
				[
					6.72639545641448,
					221.01087068256584
				],
				[
					2.8827225534539593,
					221.97175678453937
				],
				[
					-0.960950349506561,
					221.97175678453937
				],
				[
					-2.8827225534539593,
					221.97175678453937
				],
				[
					-8.648231907894797,
					221.97175678453937
				],
				[
					-13.452855160361878,
					221.97175678453937
				],
				[
					-15.374691611842195,
					221.97175678453937
				],
				[
					-19.218364514802715,
					221.97175678453937
				],
				[
					-21.14020096628292,
					221.97175678453937
				],
				[
					-22.10108706825656,
					221.97175678453937
				],
				[
					-24.98380962171052,
					221.97175678453937
				],
				[
					-26.905646073190837,
					221.01087068256584
				],
				[
					-30.749318976151358,
					216.20618318256584
				],
				[
					-33.632105777138236,
					213.32352487664457
				],
				[
					-34.59299187911188,
					211.40162417763145
				],
				[
					-34.59299187911188,
					210.44073807565792
				],
				[
					-35.55394222861844,
					207.55795127467104
				],
				[
					-35.55394222861844,
					206.59706517269728
				],
				[
					-35.55394222861844,
					204.67529296875
				],
				[
					-34.59299187911188,
					203.7142783717104
				],
				[
					-34.59299187911188,
					202.75339226973688
				],
				[
					-34.59299187911188,
					202.75339226973688
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 156,
			"versionNonce": 343422284,
			"isDeleted": false,
			"id": "kPs-WCQqF-EAQPOB2T6Fp",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 427.66780202071914,
			"y": 1889.7587172930184,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 147.020263671875,
			"height": 210.44080232319084,
			"seed": 420495988,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					14.413677014802715
				],
				[
					0,
					17.296463815789366
				],
				[
					0,
					18.257349917763122
				],
				[
					0,
					19.218364514802715
				],
				[
					0,
					20.179250616776244
				],
				[
					0.9608861019736423,
					20.179250616776244
				],
				[
					1.9218364514802033,
					20.179250616776244
				],
				[
					2.8827225534539593,
					20.179250616776244
				],
				[
					3.8436729029605203,
					20.179250616776244
				],
				[
					4.804559004934163,
					20.179250616776244
				],
				[
					5.765509354440724,
					20.179250616776244
				],
				[
					6.72639545641448,
					20.179250616776244
				],
				[
					7.687345805921041,
					20.179250616776244
				],
				[
					8.648231907894683,
					20.179250616776244
				],
				[
					9.609182257401244,
					20.179250616776244
				],
				[
					10.570068359375,
					20.179250616776244
				],
				[
					12.491904810855203,
					20.179250616776244
				],
				[
					13.452855160361764,
					20.179250616776244
				],
				[
					13.452855160361764,
					19.218364514802715
				],
				[
					13.452855160361764,
					15.374691611842081
				],
				[
					13.452855160361764,
					10.570004111842081
				],
				[
					13.452855160361764,
					6.726331208881675
				],
				[
					14.41374126233552,
					3.8436729029604066
				],
				[
					14.41374126233552,
					1.9217722039472847
				],
				[
					14.41374126233552,
					0.960886101973756
				],
				[
					15.374627364309163,
					-1.921900699013122
				],
				[
					15.374627364309163,
					-3.843672902960634
				],
				[
					15.374627364309163,
					-6.726459703947285
				],
				[
					15.374627364309163,
					-8.648231907894797
				],
				[
					15.374627364309163,
					-10.570132606907919
				],
				[
					17.29646381578948,
					-13.452919407894797
				],
				[
					17.29646381578948,
					-14.413805509868325
				],
				[
					17.29646381578948,
					-17.296463815789593
				],
				[
					18.25741416529604,
					-21.14013671875
				],
				[
					19.218300267269683,
					-24.983809621710634
				],
				[
					19.218300267269683,
					-27.866596422697285
				],
				[
					20.179250616776244,
					-32.671155427631675
				],
				[
					20.179250616776244,
					-35.553942228618325
				],
				[
					22.10108706825656,
					-40.358501233552715
				],
				[
					23.061973170230203,
					-42.28040193256584
				],
				[
					23.061973170230203,
					-45.16306023848688
				],
				[
					23.061973170230203,
					-46.124074835526244
				],
				[
					24.022923519736764,
					-48.045847039473756
				],
				[
					24.022923519736764,
					-49.96774773848688
				],
				[
					24.022923519736764,
					-51.88951994243416
				],
				[
					24.022923519736764,
					-52.85040604440792
				],
				[
					23.061973170230203,
					-53.811420641447285
				],
				[
					22.10108706825656,
					-54.77230674342104
				],
				[
					21.14013671875,
					-55.7331928453948
				],
				[
					19.218300267269683,
					-56.694078947368325
				],
				[
					18.25741416529604,
					-56.694078947368325
				],
				[
					16.335577713815724,
					-57.65496504934208
				],
				[
					17.29646381578948,
					-58.615979646381675
				],
				[
					19.218300267269683,
					-60.53775185032896
				],
				[
					22.10108706825656,
					-61.498637952302715
				],
				[
					23.061973170230203,
					-61.498637952302715
				],
				[
					25.94475997121708,
					-61.498637952302715
				],
				[
					31.71026932565792,
					-62.45965254934208
				],
				[
					32.67115542763156,
					-63.42053865131584
				],
				[
					29.7884328741776,
					-65.34231085526312
				],
				[
					28.82748252467104,
					-66.30332545230272
				],
				[
					26.905646073190724,
					-66.30332545230272
				],
				[
					25.94475997121708,
					-67.26421155427624
				],
				[
					25.94475997121708,
					-69.18598375822376
				],
				[
					25.94475997121708,
					-70.14699835526312
				],
				[
					26.905646073190724,
					-71.10788445723688
				],
				[
					27.866596422697285,
					-71.10788445723688
				],
				[
					26.905646073190724,
					-71.10788445723688
				],
				[
					21.14013671875,
					-72.0687705592104
				],
				[
					17.29646381578948,
					-73.02965666118416
				],
				[
					14.41374126233552,
					-73.02965666118416
				],
				[
					13.452855160361764,
					-73.02965666118416
				],
				[
					14.41374126233552,
					-73.99067125822376
				],
				[
					17.29646381578948,
					-74.95155736019728
				],
				[
					20.179250616776244,
					-75.91244346217104
				],
				[
					22.10108706825656,
					-75.91244346217104
				],
				[
					23.061973170230203,
					-75.91244346217104
				],
				[
					20.179250616776244,
					-75.91244346217104
				],
				[
					18.25741416529604,
					-75.91244346217104
				],
				[
					17.29646381578948,
					-76.8733295641448
				],
				[
					18.25741416529604,
					-81.67788856907896
				],
				[
					19.218300267269683,
					-83.59978926809208
				],
				[
					20.179250616776244,
					-86.48257606907896
				],
				[
					21.14013671875,
					-87.44346217105272
				],
				[
					22.10108706825656,
					-89.365234375
				],
				[
					23.061973170230203,
					-90.32624897203937
				],
				[
					22.10108706825656,
					-90.32624897203937
				],
				[
					20.179250616776244,
					-90.32624897203937
				],
				[
					18.25741416529604,
					-91.28713507401312
				],
				[
					17.29646381578948,
					-92.24802117598688
				],
				[
					16.335577713815724,
					-92.24802117598688
				],
				[
					13.452855160361764,
					-93.2089072779604
				],
				[
					12.491904810855203,
					-93.2089072779604
				],
				[
					7.687345805921041,
					-95.13080797697376
				],
				[
					6.72639545641448,
					-95.13080797697376
				],
				[
					5.765509354440724,
					-95.13080797697376
				],
				[
					3.8436729029605203,
					-97.05258018092104
				],
				[
					0,
					-97.05258018092104
				],
				[
					-5.765509354440837,
					-98.97448087993416
				],
				[
					-11.531018708881561,
					-100.89625308388145
				],
				[
					-18.25741416529604,
					-102.8181537828948
				],
				[
					-20.179250616776358,
					-102.8181537828948
				],
				[
					-25.94475997121708,
					-103.77903988486833
				],
				[
					-40.3585012335526,
					-106.6618266858552
				],
				[
					-48.04584703947364,
					-107.62271278782896
				],
				[
					-59.57686574835532,
					-109.54448499177624
				],
				[
					-62.45958830180916,
					-109.54448499177624
				],
				[
					-71.10782020970396,
					-112.42727179276312
				],
				[
					-76.87332956414468,
					-115.31005859375
				],
				[
					-83.59978926809208,
					-119.1537314967104
				],
				[
					-86.48251182154604,
					-121.07550370065792
				],
				[
					-96.0916940789474,
					-126.84107730263167
				],
				[
					-99.93536698190792,
					-132.6065224095396
				],
				[
					-101.85720343338812,
					-133.56740851151312
				],
				[
					-104.73992598684208,
					-136.4501953125
				],
				[
					-104.73992598684208,
					-137.41108141447376
				],
				[
					-107.62271278782896,
					-143.17665501644728
				],
				[
					-107.62271278782896,
					-144.13754111842104
				],
				[
					-108.5835988898026,
					-147.02032791940792
				],
				[
					-109.54448499177636,
					-154.70760947779604
				],
				[
					-110.50543534128292,
					-162.39495528371708
				],
				[
					-111.46632144325656,
					-165.27767783717104
				],
				[
					-112.42727179276312,
					-169.12135074013167
				],
				[
					-113.38815789473688,
					-171.04318719161165
				],
				[
					-113.38815789473688,
					-172.96502364309208
				],
				[
					-113.38815789473688,
					-173.92597399259876
				],
				[
					-114.34910824424344,
					-178.73053299753292
				],
				[
					-113.38815789473688,
					-179.6914833470396
				],
				[
					-110.50543534128292,
					-180.65236944901312
				],
				[
					-108.5835988898026,
					-180.65236944901312
				],
				[
					-105.70087633634864,
					-181.61325555098665
				],
				[
					-100.89625308388156,
					-181.61325555098665
				],
				[
					-96.0916940789474,
					-182.57420590049333
				],
				[
					-90.32618472450656,
					-184.49604235197376
				],
				[
					-84.56067537006584,
					-185.45692845394728
				],
				[
					-83.59978926809208,
					-185.45692845394728
				],
				[
					-80.7170024671052,
					-185.45692845394728
				],
				[
					-73.99060701069084,
					-185.45692845394728
				],
				[
					-72.06877055921052,
					-185.45692845394728
				],
				[
					-70.14693410773032,
					-185.45692845394728
				],
				[
					-69.18598375822364,
					-185.45692845394728
				],
				[
					-68.22509765625,
					-185.45692845394728
				],
				[
					-65.34237510279604,
					-186.41787880345396
				],
				[
					-58.61591539884864,
					-187.3787649054275
				],
				[
					-51.88951994243416,
					-189.30060135690792
				],
				[
					-46.12401058799344,
					-190.2615517064146
				],
				[
					-45.1631244860198,
					-190.2615517064146
				],
				[
					-41.31945158305916,
					-190.2615517064146
				],
				[
					-40.3585012335526,
					-190.2615517064146
				],
				[
					-39.39761513157896,
					-190.2615517064146
				],
				[
					-37.47577868009864,
					-190.2615517064146
				],
				[
					-37.47577868009864,
					-190.2615517064146
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 910792052,
			"isDeleted": false,
			"id": "1c-2TzwrA6ryxJlHJv2FF",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 365.20821371891,
			"y": 1893.6023901959788,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 104.73992598684208,
			"height": 235.42461194490124,
			"seed": 94820724,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					8.648231907894683,
					15.374691611842309
				],
				[
					9.609182257401244,
					16.335577713815837
				],
				[
					10.570068359375,
					16.335577713815837
				],
				[
					12.491904810855203,
					13.45279091282896
				],
				[
					14.41374126233552,
					10.570004111842309
				],
				[
					17.296463815789366,
					4.80455900493439
				],
				[
					20.179250616776244,
					0
				],
				[
					22.10108706825656,
					-3.8436729029604066
				],
				[
					22.10108706825656,
					-6.726459703947285
				],
				[
					22.10108706825656,
					-7.687345805921041
				],
				[
					22.10108706825656,
					-8.64823190789457
				],
				[
					22.10108706825656,
					-10.570132606907691
				],
				[
					22.10108706825656,
					-14.413805509868325
				],
				[
					22.10108706825656,
					-19.218364514802488
				],
				[
					21.14013671875,
					-22.101151315789366
				],
				[
					21.14013671875,
					-24.02292351973665
				],
				[
					20.179250616776244,
					-30.749383223684163
				],
				[
					18.25741416529604,
					-38.4367290296052
				],
				[
					16.335577713815724,
					-44.20217413651312
				],
				[
					15.374627364309163,
					-46.124074835526244
				],
				[
					12.491904810855203,
					-54.77230674342104
				],
				[
					10.570068359375,
					-59.5768657483552
				],
				[
					8.648231907894683,
					-63.42053865131561
				],
				[
					0,
					-79.75611636513145
				],
				[
					-5.765509354440837,
					-90.32624897203937
				],
				[
					-7.687345805921154,
					-92.24802117598665
				],
				[
					-8.648231907894797,
					-93.2089072779604
				],
				[
					-10.570068359375,
					-96.09169407894728
				],
				[
					-13.452855160361878,
					-98.0135947779604
				],
				[
					-15.374691611842195,
					-98.97448087993416
				],
				[
					-20.179250616776358,
					-101.8571391858552
				],
				[
					-22.101087068256675,
					-102.81815378289457
				],
				[
					-25.944759971217195,
					-104.73992598684185
				],
				[
					-31.71026932565792,
					-106.6618266858552
				],
				[
					-38.4366647820724,
					-109.54448499177624
				],
				[
					-48.045847039473756,
					-113.38815789473665
				],
				[
					-53.81135639391448,
					-118.19284539473665
				],
				[
					-69.18598375822376,
					-131.6456363075656
				],
				[
					-78.795166015625,
					-142.21576891447353
				],
				[
					-81.67795281661188,
					-148.94210012335498
				],
				[
					-82.63883891858552,
					-155.6685598273025
				],
				[
					-82.63883891858552,
					-157.5903962787827
				],
				[
					-82.63883891858552,
					-159.5122327302629
				],
				[
					-81.67795281661188,
					-172.00413754111833
				],
				[
					-79.75611636513156,
					-176.8086965460525
				],
				[
					-74.95149311266448,
					-183.53515625
				],
				[
					-72.06877055921052,
					-188.33971525493416
				],
				[
					-68.22509765625,
					-193.14427425986833
				],
				[
					-60.53775185032896,
					-202.75345651726957
				],
				[
					-57.655029296875,
					-205.63617907072353
				],
				[
					-51.889519942434276,
					-212.3626387746708
				],
				[
					-48.045847039473756,
					-215.24536132812477
				],
				[
					-44.202174136513236,
					-219.0890342310854
				],
				[
					-43.24128803453948,
					-219.0890342310854
				],
				[
					-32.671155427631675,
					-219.0890342310854
				],
				[
					-24.022923519736878,
					-219.0890342310854
				],
				[
					-21.14020096628292,
					-219.0890342310854
				],
				[
					-19.218364514802715,
					-219.0890342310854
				],
				[
					-11.531018708881675,
					-218.12814812911165
				],
				[
					-2.882786800986878,
					-217.16719777960498
				],
				[
					1.9218364514802033,
					-217.16719777960498
				],
				[
					6.726395456414366,
					-217.16719777960498
				],
				[
					8.648231907894683,
					-217.16719777960498
				],
				[
					12.491904810855203,
					-217.16719777960498
				],
				[
					13.452855160361764,
					-217.16719777960498
				],
				[
					14.41374126233552,
					-218.12814812911165
				],
				[
					17.296463815789366,
					-218.12814812911165
				],
				[
					19.218300267269683,
					-218.12814812911165
				],
				[
					21.14013671875,
					-219.0890342310854
				],
				[
					21.14013671875,
					-219.0890342310854
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1557900236,
			"isDeleted": false,
			"id": "H3DeYAFPO6mdKAXQHVXSi",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 294.100393509206,
			"y": 1881.1104853851236,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 151.82482267680916,
			"height": 259.4474712171052,
			"seed": 1794213236,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					16.335577713815724,
					34.59292763157896
				],
				[
					19.218300267269683,
					30.749254728618553
				],
				[
					23.061973170230203,
					23.061908922697512
				],
				[
					27.86653217516448,
					11.531018708881675
				],
				[
					35.55387798108552,
					-9.609246504934163
				],
				[
					38.436664782072285,
					-21.140265213815837
				],
				[
					39.39755088404604,
					-27.866596422697285
				],
				[
					40.3585012335526,
					-46.124074835526244
				],
				[
					40.3585012335526,
					-49.96774773848688
				],
				[
					40.3585012335526,
					-57.65509354440792
				],
				[
					40.3585012335526,
					-67.26421155427624
				],
				[
					39.39755088404604,
					-77.83434416118416
				],
				[
					37.475714432565724,
					-82.63890316611833
				],
				[
					34.592991879111764,
					-87.44346217105249
				],
				[
					28.82748252467104,
					-96.09169407894728
				],
				[
					26.905646073190724,
					-99.93536698190792
				],
				[
					8.648231907894683,
					-110.50549958881561
				],
				[
					1.9218364514802033,
					-113.38815789473688
				],
				[
					-0.960950349506561,
					-115.31005859374977
				],
				[
					-17.2965280633224,
					-122.03651829769728
				],
				[
					-31.71026932565792,
					-127.8019634046052
				],
				[
					-41.31945158305916,
					-131.6456363075656
				],
				[
					-49.96768349095396,
					-136.45019531249977
				],
				[
					-56.69414319490136,
					-141.25481856496685
				],
				[
					-57.655029296875,
					-142.2157046669406
				],
				[
					-60.53775185032896,
					-147.98121402138145
				],
				[
					-62.45958830180916,
					-152.7857730263156
				],
				[
					-62.45958830180916,
					-153.74672337582228
				],
				[
					-62.45958830180916,
					-155.6685598273025
				],
				[
					-61.49870219983552,
					-163.35590563322353
				],
				[
					-61.49870219983552,
					-165.27774208470396
				],
				[
					-59.57686574835532,
					-172.00413754111833
				],
				[
					-55.73319284539468,
					-183.53515624999977
				],
				[
					-53.81135639391448,
					-186.41787880345396
				],
				[
					-51.88951994243416,
					-189.3006656044406
				],
				[
					-46.12401058799344,
					-198.90978361430894
				],
				[
					-33.63210577713812,
					-207.55807976973688
				],
				[
					-26.905710320723642,
					-212.36263877467104
				],
				[
					-20.179250616776358,
					-215.24536132812477
				],
				[
					-14.413805509868439,
					-217.1671977796052
				],
				[
					-3.8436729029605203,
					-219.0890342310854
				],
				[
					-0.960950349506561,
					-219.0890342310854
				],
				[
					7.687281558388122,
					-219.0890342310854
				],
				[
					12.491904810855203,
					-219.0890342310854
				],
				[
					17.29646381578948,
					-220.04998458059185
				],
				[
					24.98380962171052,
					-221.0108706825656
				],
				[
					36.51482833059208,
					-222.93270713404604
				],
				[
					41.319387335526244,
					-224.85454358552624
				],
				[
					44.20217413651312,
					-224.85454358552624
				],
				[
					47.08489668996708,
					-224.85454358552624
				],
				[
					51.889455694901244,
					-224.85454358552624
				],
				[
					54.77224249588812,
					-224.85454358552624
				],
				[
					63.420474403782805,
					-224.85454358552624
				],
				[
					76.87332956414468,
					-224.85454358552624
				],
				[
					77.83421566611833,
					-224.85454358552624
				],
				[
					78.795166015625,
					-224.85454358552624
				],
				[
					80.7170024671052,
					-224.85454358552624
				],
				[
					81.67788856907896,
					-224.85454358552624
				],
				[
					83.59972502055916,
					-224.85454358552624
				],
				[
					87.44339792351968,
					-224.85454358552624
				],
				[
					89.365234375,
					-224.85454358552624
				],
				[
					89.365234375,
					-224.85454358552624
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 819906292,
			"isDeleted": false,
			"id": "4rURj6tKzMtkI-VNOMwDw",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 303.70951151907445,
			"y": 1388.1601744270647,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 84.56067537006572,
			"height": 151.82482267680916,
			"seed": 1991138252,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					27.866596422697285,
					2.882722553453732
				],
				[
					30.749383223684163,
					3.8436729029604066
				],
				[
					31.710269325657805,
					3.8436729029604066
				],
				[
					37.47577868009864,
					4.804559004934163
				],
				[
					38.436664782072285,
					4.804559004934163
				],
				[
					39.397615131578846,
					5.765509354440837
				],
				[
					39.397615131578846,
					9.609182257401244
				],
				[
					39.397615131578846,
					20.179250616776244
				],
				[
					39.397615131578846,
					24.983809621710407
				],
				[
					39.397615131578846,
					29.788432874177488
				],
				[
					38.436664782072285,
					36.51482833059208
				],
				[
					37.47577868009864,
					38.436664782072285
				],
				[
					36.51482833059208,
					40.35850123355249
				],
				[
					31.710269325657805,
					49.006733141447285
				],
				[
					24.983873869243325,
					58.615915398848756
				],
				[
					24.022923519736764,
					59.576801500822285
				],
				[
					20.179250616776244,
					64.38142475328937
				],
				[
					18.25741416529604,
					67.26414730674333
				],
				[
					16.335577713815724,
					72.0687705592104
				],
				[
					14.413805509868325,
					76.87332956414457
				],
				[
					11.531018708881561,
					86.48251182154581
				],
				[
					9.609182257401244,
					98.97441663240124
				],
				[
					9.609182257401244,
					101.8571391858552
				],
				[
					9.609182257401244,
					110.50543534128292
				],
				[
					9.609182257401244,
					114.34910824424333
				],
				[
					10.570132606907805,
					122.9973401521379
				],
				[
					12.491969058388122,
					133.5674085115129
				],
				[
					14.413805509868325,
					137.41108141447353
				],
				[
					18.25741416529604,
					144.1374768708879
				],
				[
					19.2183645148026,
					145.09842722039457
				],
				[
					23.062037417763122,
					147.98114977384853
				],
				[
					27.866596422697285,
					150.8639365748354
				],
				[
					31.710269325657805,
					151.82482267680916
				],
				[
					35.553942228618325,
					151.82482267680916
				],
				[
					42.280337685032805,
					151.82482267680916
				],
				[
					47.0849609375,
					151.82482267680916
				],
				[
					55.73319284539468,
					151.82482267680916
				],
				[
					60.537751850328846,
					150.8639365748354
				],
				[
					67.26421155427624,
					148.94210012335498
				],
				[
					75.91244346217104,
					147.020263671875
				],
				[
					76.87332956414468,
					147.020263671875
				],
				[
					82.63883891858552,
					146.05931332236833
				],
				[
					84.56067537006572,
					145.09842722039457
				],
				[
					84.56067537006572,
					145.09842722039457
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1720472140,
			"isDeleted": false,
			"id": "SnciLg_B-e7pMCknNqq4x",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 297.94406641216653,
			"y": 1435.2450711170318,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 102.81808953536188,
			"height": 150.8639365748354,
			"seed": 1025464012,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					13.45285516036165
				],
				[
					-0.960950349506561,
					17.296528063322285
				],
				[
					-2.882786800986878,
					23.062037417763122
				],
				[
					-4.804623252467081,
					34.59299187911165
				],
				[
					-5.765509354440837,
					41.31945158305916
				],
				[
					-10.570132606907919,
					55.73319284539457
				],
				[
					-12.491969058388122,
					61.49870219983541
				],
				[
					-15.374691611842081,
					70.1469341077302
				],
				[
					-18.25747841282896,
					74.95149311266437
				],
				[
					-19.2183645148026,
					76.87332956414457
				],
				[
					-20.179314864309163,
					88.40434827302624
				],
				[
					-21.14020096628292,
					93.2089072779604
				],
				[
					-21.14020096628292,
					95.13074372944084
				],
				[
					-21.14020096628292,
					103.77903988486833
				],
				[
					-21.14020096628292,
					107.62271278782873
				],
				[
					-19.2183645148026,
					122.9973401521379
				],
				[
					-18.25747841282896,
					124.91917660361833
				],
				[
					-16.335641961348642,
					126.84101305509853
				],
				[
					-13.452855160361878,
					133.5674085115129
				],
				[
					-12.491969058388122,
					134.52835886101957
				],
				[
					-9.609182257401358,
					138.3720317639802
				],
				[
					-3.8436729029605203,
					144.1375411184208
				],
				[
					-0.960950349506561,
					145.09842722039457
				],
				[
					0.9608861019736423,
					146.05937756990124
				],
				[
					7.687281558388122,
					148.9421001233552
				],
				[
					13.45279091282896,
					150.8639365748354
				],
				[
					18.25741416529604,
					150.8639365748354
				],
				[
					31.710205078125,
					147.98121402138145
				],
				[
					37.475714432565724,
					147.020263671875
				],
				[
					40.3585012335526,
					147.020263671875
				],
				[
					42.2802734375,
					147.020263671875
				],
				[
					44.2021098889802,
					147.020263671875
				],
				[
					50.9285695929276,
					147.020263671875
				],
				[
					58.61591539884864,
					146.05937756990124
				],
				[
					60.53775185032896,
					145.09842722039457
				],
				[
					62.459524054276244,
					144.1375411184208
				],
				[
					64.38136050575656,
					144.1375411184208
				],
				[
					68.22503340871708,
					143.17659076891437
				],
				[
					71.10782020970396,
					143.17659076891437
				],
				[
					72.0687063116776,
					143.17659076891437
				],
				[
					74.95149311266448,
					142.21570466694084
				],
				[
					76.87332956414468,
					142.21570466694084
				],
				[
					77.83421566611844,
					142.21570466694084
				],
				[
					78.795166015625,
					142.21570466694084
				],
				[
					79.75605211759864,
					142.21570466694084
				],
				[
					80.7170024671052,
					142.21570466694084
				],
				[
					81.67788856907896,
					141.25475431743416
				],
				[
					81.67788856907896,
					141.25475431743416
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1423034484,
			"isDeleted": false,
			"id": "Ug8ov0KLMawMG_vHejuZV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 92.30785521767643,
			"y": 1376.629155718183,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 9.609182257401358,
			"height": 111.46632144325667,
			"seed": 1811139532,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9218364514802602,
					-26.905646073190837
				],
				[
					2.8827546772204187,
					-37.47571443256584
				],
				[
					7.6873458059210975,
					-62.45958830180916
				],
				[
					9.609182257401358,
					-96.09169407894728
				],
				[
					9.609182257401358,
					-102.81808953536165
				],
				[
					9.609182257401358,
					-109.54448499177624
				],
				[
					9.609182257401358,
					-111.46632144325667
				],
				[
					9.609182257401358,
					-111.46632144325667
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 23,
			"versionNonce": 1885612236,
			"isDeleted": false,
			"id": "GKtjnW1MZti1Umk4Gs2XH",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 96.15152812063695,
			"y": 1265.1628342749264,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 69.18601588199016,
			"height": 39.39755088404627,
			"seed": 2143665356,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					47.08492881373354,
					0
				],
				[
					51.88948781866776,
					0
				],
				[
					55.73316072162828,
					0
				],
				[
					61.49867007606906,
					0
				],
				[
					64.38139262952302,
					0
				],
				[
					67.2641794305099,
					0
				],
				[
					68.22506553248354,
					0
				],
				[
					69.18601588199016,
					0.960886101973756
				],
				[
					69.18601588199016,
					3.843672902960634
				],
				[
					69.18601588199016,
					8.648231907895024
				],
				[
					69.18601588199016,
					14.413741262335634
				],
				[
					69.18601588199016,
					19.218300267270024
				],
				[
					69.18601588199016,
					24.022923519737105
				],
				[
					69.18601588199016,
					29.788432874177943
				],
				[
					69.18601588199016,
					33.63210577713835
				],
				[
					69.18601588199016,
					34.592991879112105
				],
				[
					69.18601588199016,
					36.51482833059208
				],
				[
					69.18601588199016,
					39.39755088404627
				],
				[
					69.18601588199016,
					39.39755088404627
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 6,
			"versionNonce": 1441307124,
			"isDeleted": false,
			"id": "rTBbfKvvZj6fTV2O6JqMp",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 132.6663564512291,
			"y": 1317.0523542173607,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 58.615947522615045,
			"height": 8.648296155427715,
			"seed": 525346124,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					58.615947522615045,
					-8.648296155427715
				],
				[
					58.615947522615045,
					-8.648296155427715
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1308438348,
			"isDeleted": false,
			"id": "6hd__CAXfEb3d4xVm9BA6",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 149.00193416504487,
			"y": 1321.856913222295,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 38.436696905838744,
			"height": 0,
			"seed": 1969037132,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					5.7655093544407805,
					0
				],
				[
					8.648264031661142,
					0
				],
				[
					16.33560983758224,
					0
				],
				[
					24.02295564350328,
					0
				],
				[
					30.74935109991776,
					0
				],
				[
					34.593024002878224,
					0
				],
				[
					38.436696905838744,
					0
				],
				[
					38.436696905838744,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 8,
			"versionNonce": 2133408628,
			"isDeleted": false,
			"id": "nKWlm8zDgwg43d_dKZxfP",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 159.57203464818627,
			"y": 1333.3879319311764,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 24.983809621710577,
			"height": 4.804623252467081,
			"seed": 507818060,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					23.06197317023026,
					-4.804623252467081
				],
				[
					24.02292351973682,
					-4.804623252467081
				],
				[
					24.983809621710577,
					-4.804623252467081
				],
				[
					24.983809621710577,
					-4.804623252467081
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 23,
			"versionNonce": 1337025996,
			"isDeleted": false,
			"id": "s4SrZlI8Obxjprso39gu9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 168.22026655608101,
			"y": 1391.0428969805184,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 170.08230108963812,
			"height": 62.45958830180916,
			"seed": 1032783692,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					16.335577713815837,
					-31.710205078125
				],
				[
					18.25741416529604,
					-33.632041529604976
				],
				[
					21.14020096628292,
					-39.39755088404581
				],
				[
					26.905710320723642,
					-47.08489668996708
				],
				[
					28.82748252467104,
					-49.00673314144706
				],
				[
					32.67115542763156,
					-51.889455694901244
				],
				[
					46.12401058799344,
					-54.772242495887895
				],
				[
					49.0067331414474,
					-55.73312859786165
				],
				[
					55.7331928453948,
					-56.694078947368325
				],
				[
					61.49870219983552,
					-57.65496504934208
				],
				[
					80.71700246710532,
					-60.53775185032873
				],
				[
					111.46632144325656,
					-61.49863795230249
				],
				[
					140.29386821546052,
					-61.49863795230249
				],
				[
					144.13754111842104,
					-61.49863795230249
				],
				[
					158.55128238075656,
					-61.49863795230249
				],
				[
					160.47311883223676,
					-61.49863795230249
				],
				[
					168.16046463815792,
					-62.45958830180916
				],
				[
					170.08230108963812,
					-62.45958830180916
				],
				[
					170.08230108963812,
					-62.45958830180916
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 1255779572,
			"isDeleted": false,
			"id": "eP3LxaVF5QKNprB2HUhhE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 342.14617630114674,
			"y": 1304.5603851589726,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 1.921836451480317,
			"height": 57.655029296875,
			"seed": 1735778252,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.960950349506561,
					21.14020096628292
				],
				[
					0.960950349506561,
					24.02292351973665
				],
				[
					0.960950349506561,
					26.905710320723756
				],
				[
					0.960950349506561,
					32.671219675164366
				],
				[
					0.960950349506561,
					40.35850123355249
				],
				[
					0.960950349506561,
					45.16312448601957
				],
				[
					1.921836451480317,
					49.0067973889802
				],
				[
					1.921836451480317,
					49.96768349095373
				],
				[
					1.921836451480317,
					51.88951994243416
				],
				[
					1.921836451480317,
					54.77230674342081
				],
				[
					1.921836451480317,
					55.73319284539457
				],
				[
					1.921836451480317,
					56.694143194901244
				],
				[
					0.960950349506561,
					57.655029296875
				],
				[
					0.960950349506561,
					57.655029296875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 6,
			"versionNonce": 714787916,
			"isDeleted": false,
			"id": "oM6ZunRNj6qGl3TDJsiLe",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 361.36454081594945,
			"y": 1316.091403867854,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 21.140136718749886,
			"height": 0.9608861019735286,
			"seed": 1171703756,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					21.140136718749886,
					-0.9608861019735286
				],
				[
					21.140136718749886,
					-0.9608861019735286
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 6,
			"versionNonce": 2055204468,
			"isDeleted": false,
			"id": "cFpbAoqQlCgC6GpH-yANE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 375.778282078285,
			"y": 1298.7949400520647,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 28.82748252467104,
			"seed": 71205324,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					28.82748252467104
				],
				[
					0,
					28.82748252467104
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 23,
			"versionNonce": 1620271820,
			"isDeleted": false,
			"id": "fPdMhSiNuUqQSFdDpR2tG",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 405.5667149524626,
			"y": 1298.7949400520647,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 9.609182257401358,
			"height": 27.866532175164366,
			"seed": 2079931340,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.8436729029605203,
					9.609118009868325
				],
				[
					-2.882786800986878,
					10.570068359375
				],
				[
					0,
					12.491904810855203
				],
				[
					0.9608861019736423,
					13.452790912828732
				],
				[
					1.9218364514802033,
					14.413741262335407
				],
				[
					3.8436729029605203,
					15.374627364309163
				],
				[
					3.8436729029605203,
					16.335577713815837
				],
				[
					3.8436729029605203,
					17.296463815789366
				],
				[
					3.8436729029605203,
					19.21830026726957
				],
				[
					3.8436729029605203,
					21.14013671875
				],
				[
					3.8436729029605203,
					23.061973170230203
				],
				[
					2.8827225534539593,
					24.022859272203732
				],
				[
					1.9218364514802033,
					26.905646073190837
				],
				[
					0,
					26.905646073190837
				],
				[
					-0.960950349506561,
					27.866532175164366
				],
				[
					-1.921836451480317,
					27.866532175164366
				],
				[
					-2.882786800986878,
					27.866532175164366
				],
				[
					-5.765509354440837,
					26.905646073190837
				],
				[
					-5.765509354440837,
					26.905646073190837
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 6,
			"versionNonce": 786563060,
			"isDeleted": false,
			"id": "uGvs4WEof3U3SlAqzijQ8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 408.44943750591653,
			"y": 1296.8731036005843,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 30.749383223684163,
			"height": 4.804623252467081,
			"seed": 349586508,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072128217,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					30.749383223684163,
					-4.804623252467081
				],
				[
					30.749383223684163,
					-4.804623252467081
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "image",
			"version": 1,
			"versionNonce": 450090601,
			"isDeleted": false,
			"id": "OSxqfToz",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -562.466647641081,
			"y": 1915.6274176830514,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 500,
			"height": 330.35714285714283,
			"seed": 53602,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1715072210104,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "02e27d046075b40807129a36eec75f02cf77f221",
			"scale": [
				1,
				1
			]
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#e03131",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 539.4848561034097,
		"scrollY": -1656.2263442166227,
		"zoom": {
			"value": 2.077795964429402
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		},
		"objectsSnapModeEnabled": false
	},
	"files": {}
}

```

%%