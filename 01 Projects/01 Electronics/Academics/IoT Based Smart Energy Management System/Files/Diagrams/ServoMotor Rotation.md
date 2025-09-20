---
id: ServoMotor_Rotation
aliases: []
tags: [excalidraw]
excalidraw-plugin: parsed
dg-publish: true
---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==

# Text Elements
Servo ^YKZEOPbN

If I do Servo.write(current_position + 2);  ^oKtKOQeP

Servo ^skByg4G2

Solar Tracking Algorithm ^j0HYZCdt

Servo ^TUEcF4vb

If the Sun is on the top
 side Servo.write(current -1); ^5grvxoH3

If the Sun is on the right ^kRTq0oLH

side Servo.write(current -1); ^NHPTG90t

if (avg_right > avg_left) ^f3XWGXHb

Horizontal_Servo.write(current -1); ^LkLRID1J

if (avg_top > avg_bottom) ^dpPdz7dP

Vertical_Servo.write(current -1); ^h7JtK9uT

LDR System
 ^5FHRn96w

TL ^8SvqNeWq

TR ^RilH81OR

BL ^DRlk3Ano

BR ^mnEb0JZt

Servo ^zVB6YBxS

Servo ^I0zqIgVf

Ant Clcok Wise ^pCiLTmNr

%%
# Drawing

```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.1.6",
	"elements": [
		{
			"type": "rectangle",
			"version": 51,
			"versionNonce": 92732717,
			"isDeleted": false,
			"id": "UAHFy9ELBjpTOKbE5CkUg",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -119.95689392089844,
			"y": 65.10626220703125,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 132.36627197265625,
			"height": 110.45736694335938,
			"seed": 1116031504,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "TBu35_hdrUyHmHWeVhjPX",
					"type": "arrow"
				}
			],
			"updated": 1714682747195,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 8,
			"versionNonce": 769861648,
			"isDeleted": false,
			"id": "YKZEOPbN",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -71.52694702148438,
			"y": -3.337158203125,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.23994445800781,
			"height": 25,
			"seed": 857936112,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714621943620,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Servo",
			"rawText": "Servo",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Servo",
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 590,
			"versionNonce": 1445025261,
			"isDeleted": false,
			"id": "TBu35_hdrUyHmHWeVhjPX",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 3.1070404469382478,
			"x": -91.18690026411507,
			"y": -50.73458959593826,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 80.84297194779668,
			"height": 95.95168257628592,
			"seed": 815629040,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714682747196,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "UAHFy9ELBjpTOKbE5CkUg",
				"focus": 0.8225951612448397,
				"gap": 20.524011539622094
			},
			"endBinding": {
				"elementId": "UAHFy9ELBjpTOKbE5CkUg",
				"focus": -0.820711762562363,
				"gap": 25.145475642298365
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					30.03932585727916,
					95.95168257628592
				],
				[
					80.84297194779668,
					6.608923908510029
				]
			]
		},
		{
			"type": "arrow",
			"version": 47,
			"versionNonce": 385216528,
			"isDeleted": false,
			"id": "HnG0OHQzc64WyzkQNPXSE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 136.55978393554688,
			"y": -171.32733154296875,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 65.7266845703125,
			"height": 84.89697265625,
			"seed": 1024392432,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714621967480,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-65.7266845703125,
					84.89697265625
				]
			]
		},
		{
			"type": "text",
			"version": 58,
			"versionNonce": 323780848,
			"isDeleted": false,
			"id": "oKtKOQeP",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 199.47305297851562,
			"y": -198.337158203125,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 426.03955078125,
			"height": 25,
			"seed": 488975376,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622038945,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "If I do Servo.write(current_position + 2); ",
			"rawText": "If I do Servo.write(current_position + 2); ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "If I do Servo.write(current_position + 2); ",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 206,
			"versionNonce": 1538472464,
			"isDeleted": false,
			"id": "OoYBnL8Zh1CJv7DQ4K-Wl",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 4.733307795873259,
			"x": -74.20580649073786,
			"y": 199.52765451851167,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 132.36627197265625,
			"height": 110.45736694335938,
			"seed": 686691568,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "NCm4GVN_vEChuTgAmUKD9",
					"type": "arrow"
				}
			],
			"updated": 1714622420602,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 174,
			"versionNonce": 396218608,
			"isDeleted": false,
			"id": "skByg4G2",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 4.733307795873259,
			"x": -31.807453989613002,
			"y": 247.14293687682834,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.23994445800781,
			"height": 25,
			"seed": 1044248304,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622420602,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Servo",
			"rawText": "Servo",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Servo",
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 929,
			"versionNonce": 1009597168,
			"isDeleted": false,
			"id": "NCm4GVN_vEChuTgAmUKD9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5571629356319212,
			"x": -158.79486556402946,
			"y": 258.76273063337396,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 167.72142759922832,
			"height": 23.774164928933846,
			"seed": 591501552,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714622421633,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "OoYBnL8Zh1CJv7DQ4K-Wl",
				"focus": 0.8045814122836329,
				"gap": 19.22360492509418
			},
			"endBinding": {
				"elementId": "OoYBnL8Zh1CJv7DQ4K-Wl",
				"focus": -0.820711762562363,
				"gap": 25.145475642298365
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					86.13339253037987,
					-16.09274057114256
				],
				[
					167.72142759922832,
					7.681424357791285
				]
			]
		},
		{
			"type": "arrow",
			"version": 38,
			"versionNonce": 622364400,
			"isDeleted": false,
			"id": "S_GoyvcAud_0RratV_WI_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 177.68775430276105,
			"y": -151.81102706180354,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 167.63627485795456,
			"height": 282.16011740944606,
			"seed": 2018257424,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714622430571,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-167.63627485795456,
					282.16011740944606
				]
			]
		},
		{
			"type": "text",
			"version": 67,
			"versionNonce": 664515088,
			"isDeleted": false,
			"id": "j0HYZCdt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 285.6225729544575,
			"y": -7.8491624370031445,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 238.2797393798828,
			"height": 25,
			"seed": 1772662000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622563872,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Solar Tracking Algorithm",
			"rawText": "Solar Tracking Algorithm",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Solar Tracking Algorithm",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 85,
			"versionNonce": 1736385264,
			"isDeleted": false,
			"id": "t2ubpeqaLVYDPrLxPQOCt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 218.65074113561678,
			"y": 81.4454461457708,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 132.36627197265625,
			"height": 110.45736694335938,
			"seed": 1626795024,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "Y_xKfqycjXyzK0tSQU67f",
					"type": "arrow"
				}
			],
			"updated": 1714622567849,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 52,
			"versionNonce": 1063724784,
			"isDeleted": false,
			"id": "TUEcF4vb",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 253.38767961217928,
			"y": 127.11091245436455,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.23994445800781,
			"height": 25,
			"seed": 694086160,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622567849,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Servo",
			"rawText": "Servo",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Servo",
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 661,
			"versionNonce": 518011408,
			"isDeleted": false,
			"id": "Y_xKfqycjXyzK0tSQU67f",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 3.1070404469382478,
			"x": 200.23966131633097,
			"y": 72.97458644403667,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 167.72142759922832,
			"height": 23.774164928933846,
			"seed": 1612130320,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714622568011,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "t2ubpeqaLVYDPrLxPQOCt",
				"focus": 0.8145800305330879,
				"gap": 20.306542613142398
			},
			"endBinding": {
				"elementId": "t2ubpeqaLVYDPrLxPQOCt",
				"focus": -0.820711762562363,
				"gap": 25.145475642298365
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					86.13339253037987,
					-16.09274057114256
				],
				[
					167.72142759922832,
					7.681424357791285
				]
			]
		},
		{
			"type": "text",
			"version": 339,
			"versionNonce": 1156825616,
			"isDeleted": false,
			"id": "5grvxoH3",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 294.6769392966823,
			"y": 435.0303096844299,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 277.71966552734375,
			"height": 50,
			"seed": 1060459760,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622930912,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "If the Sun is on the top\n side Servo.write(current -1);",
			"rawText": "If the Sun is on the top\n side Servo.write(current -1);",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "If the Sun is on the top\n side Servo.write(current -1);",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 60,
			"versionNonce": 1607767056,
			"isDeleted": false,
			"id": "kRTq0oLH",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 308.4936585066525,
			"y": 227.13824539653422,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 257.5596923828125,
			"height": 25,
			"seed": 981305072,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622877058,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "If the Sun is on the right",
			"rawText": "If the Sun is on the right",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "If the Sun is on the right",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 60,
			"versionNonce": 1313313296,
			"isDeleted": false,
			"id": "NHPTG90t",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 308.4936585066525,
			"y": 262.1382453965342,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 267.7196960449219,
			"height": 25,
			"seed": 1530306576,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622877058,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "side Servo.write(current -1);",
			"rawText": "side Servo.write(current -1);",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "side Servo.write(current -1);",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 61,
			"versionNonce": 833277968,
			"isDeleted": false,
			"id": "f3XWGXHb",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 308.4936585066525,
			"y": 297.1382453965342,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 250.93971252441406,
			"height": 25,
			"seed": 286206192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622877058,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "if (avg_right > avg_left)",
			"rawText": "if (avg_right > avg_left)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "if (avg_right > avg_left)",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 61,
			"versionNonce": 32919056,
			"isDeleted": false,
			"id": "LkLRID1J",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 308.4936585066525,
			"y": 332.1382453965342,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 333.5196228027344,
			"height": 25,
			"seed": 696786448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622877058,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Horizontal_Servo.write(current -1);",
			"rawText": "Horizontal_Servo.write(current -1);",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Horizontal_Servo.write(current -1);",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 59,
			"versionNonce": 832837136,
			"isDeleted": false,
			"id": "dpPdz7dP",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 305.15582019750065,
			"y": 499.9727616493243,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 269.35968017578125,
			"height": 25,
			"seed": 2136374800,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622935308,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "if (avg_top > avg_bottom)",
			"rawText": "if (avg_top > avg_bottom)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "if (avg_top > avg_bottom)",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 59,
			"versionNonce": 2128008208,
			"isDeleted": false,
			"id": "h7JtK9uT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 305.15582019750065,
			"y": 534.9727616493243,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 310.8796691894531,
			"height": 25,
			"seed": 635710192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714622935308,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Vertical_Servo.write(current -1);",
			"rawText": "Vertical_Servo.write(current -1);",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Vertical_Servo.write(current -1);",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 33,
			"versionNonce": 1634505456,
			"isDeleted": false,
			"id": "OFKjupQmQmdjlYClHe0kN",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -111.05613731455225,
			"y": 620.8162059833362,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 193.05557250976557,
			"height": 244.44442749023426,
			"seed": 1010586864,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "5FHRn96w"
				}
			],
			"updated": 1714623144119,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 13,
			"versionNonce": 1040783376,
			"isDeleted": false,
			"id": "5FHRn96w",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -73.74829124521634,
			"y": 718.0384197284534,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 118.43988037109375,
			"height": 50,
			"seed": 1014797552,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623143893,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "LDR System\n",
			"rawText": "LDR System\n",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "OFKjupQmQmdjlYClHe0kN",
			"originalText": "LDR System\n",
			"lineHeight": 1.25
		},
		{
			"type": "freedraw",
			"version": 145,
			"versionNonce": 2110469136,
			"isDeleted": false,
			"id": "x7KA725asFyQc5_KZGLpi",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 120.88829017568207,
			"y": 872.205060963805,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 216.66666666666663,
			"height": 101.38885498046864,
			"seed": 507294960,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623154611,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-102.77776082356763,
					-30.55552164713538
				],
				[
					-144.44442749023432,
					-38.888854980468636
				],
				[
					-159.72218831380206,
					-38.888854980468636
				],
				[
					-174.99999999999994,
					-37.499999999999886
				],
				[
					-184.72218831380206,
					-36.111094156901004
				],
				[
					-198.611094156901,
					-31.94442749023426
				],
				[
					-202.77776082356763,
					-29.16666666666663
				],
				[
					-206.94442749023432,
					-27.777760823567633
				],
				[
					-209.722188313802,
					-24.999999999999886
				],
				[
					-211.111094156901,
					-23.611094156901004
				],
				[
					-201.3888549804687,
					-19.444427490234375
				],
				[
					-180.55552164713538,
					-15.277760823567633
				],
				[
					-127.77776082356769,
					-15.277760823567633
				],
				[
					-109.72218831380201,
					-15.277760823567633
				],
				[
					-87.5,
					-18.05552164713538
				],
				[
					-84.72218831380201,
					-18.05552164713538
				],
				[
					-83.33333333333326,
					-18.05552164713538
				],
				[
					-81.94442749023438,
					-18.05552164713538
				],
				[
					-98.611094156901,
					-23.611094156901004
				],
				[
					-148.611094156901,
					-30.55552164713538
				],
				[
					-168.05552164713538,
					-30.55552164713538
				],
				[
					-184.72218831380206,
					-27.777760823567633
				],
				[
					-202.77776082356763,
					-23.611094156901004
				],
				[
					-208.33333333333326,
					-22.222188313802008
				],
				[
					-212.49999999999994,
					-19.444427490234375
				],
				[
					-215.27776082356763,
					-18.05552164713538
				],
				[
					-216.66666666666663,
					-16.66666666666663
				],
				[
					-177.7777608235677,
					0
				],
				[
					-151.3888549804687,
					4.1666666666667425
				],
				[
					-112.5,
					5.555572509765625
				],
				[
					-98.611094156901,
					4.1666666666667425
				],
				[
					-80.55552164713538,
					0
				],
				[
					-72.22218831380201,
					-4.166666666666629
				],
				[
					-70.83333333333326,
					-6.944427490234375
				],
				[
					-80.55552164713538,
					-18.05552164713538
				],
				[
					-102.77776082356763,
					-24.999999999999886
				],
				[
					-127.77776082356769,
					-26.388854980468636
				],
				[
					-169.44442749023432,
					-19.444427490234375
				],
				[
					-183.33333333333331,
					-13.88885498046875
				],
				[
					-199.99999999999994,
					-2.7777608235676325
				],
				[
					-208.33333333333326,
					2.7778116861979925
				],
				[
					-211.111094156901,
					5.555572509765625
				],
				[
					-212.49999999999994,
					6.944478352864621
				],
				[
					-212.49999999999994,
					9.722239176432367
				],
				[
					-194.44442749023432,
					23.61114501953125
				],
				[
					-156.94442749023432,
					37.5
				],
				[
					-112.5,
					48.61114501953125
				],
				[
					-81.94442749023438,
					54.16666666666674
				],
				[
					-47.22218831380201,
					55.555572509765625
				],
				[
					-44.444427490234375,
					55.555572509765625
				],
				[
					-40.27776082356763,
					54.16666666666674
				],
				[
					-45.83333333333326,
					43.055572509765625
				],
				[
					-65.27776082356763,
					31.94447835286462
				],
				[
					-88.88885498046875,
					22.222239176432367
				],
				[
					-127.77776082356769,
					15.277811686197992
				],
				[
					-143.05552164713538,
					15.277811686197992
				],
				[
					-158.33333333333331,
					16.666666666666742
				],
				[
					-168.05552164713538,
					20.83333333333337
				],
				[
					-174.99999999999994,
					23.61114501953125
				],
				[
					-183.33333333333331,
					27.777811686197992
				],
				[
					-184.72218831380206,
					29.166666666666742
				],
				[
					-186.111094156901,
					29.166666666666742
				],
				[
					-187.49999999999994,
					30.555572509765625
				],
				[
					-179.16666666666663,
					38.888905843098996
				],
				[
					-116.66666666666663,
					59.72223917643237
				],
				[
					-88.88885498046875,
					62.5
				],
				[
					-72.22218831380201,
					61.11114501953125
				],
				[
					-41.66666666666663,
					54.16666666666674
				],
				[
					-31.944427490234375,
					48.61114501953125
				],
				[
					-26.38885498046875,
					44.44447835286462
				],
				[
					-20.833333333333258,
					30.555572509765625
				],
				[
					-25,
					22.222239176432367
				],
				[
					-33.33333333333326,
					12.5
				],
				[
					-79.16666666666663,
					-9.722188313802008
				],
				[
					-100,
					-12.5
				],
				[
					-129.16666666666663,
					-11.111094156901004
				],
				[
					-138.8888549804687,
					-9.722188313802008
				],
				[
					-151.3888549804687,
					-6.944427490234375
				],
				[
					-154.16666666666663,
					-4.166666666666629
				],
				[
					-155.55552164713538,
					-4.166666666666629
				],
				[
					-156.94442749023432,
					-2.7777608235676325
				],
				[
					-158.33333333333331,
					-2.7777608235676325
				],
				[
					-158.33333333333331,
					-1.38885498046875
				],
				[
					-151.3888549804687,
					8.333333333333371
				],
				[
					-136.111094156901,
					22.222239176432367
				],
				[
					-97.22218831380201,
					44.44447835286462
				],
				[
					-87.5,
					47.22223917643237
				],
				[
					-80.55552164713538,
					48.61114501953125
				],
				[
					-70.83333333333326,
					48.61114501953125
				],
				[
					-66.66666666666663,
					47.22223917643237
				],
				[
					-61.111094156901004,
					36.11114501953125
				],
				[
					-58.33333333333326,
					27.777811686197992
				],
				[
					-58.33333333333326,
					19.44447835286462
				],
				[
					-61.111094156901004,
					11.11114501953125
				],
				[
					-75,
					-6.944427490234375
				],
				[
					-88.88885498046875,
					-15.277760823567633
				],
				[
					-119.44442749023438,
					-18.05552164713538
				],
				[
					-130.55552164713538,
					-16.66666666666663
				],
				[
					-138.8888549804687,
					-13.88885498046875
				],
				[
					-145.83333333333331,
					-11.111094156901004
				],
				[
					-155.55552164713538,
					-6.944427490234375
				],
				[
					-156.94442749023432,
					-5.555521647135379
				],
				[
					-158.33333333333331,
					-5.555521647135379
				],
				[
					-159.72218831380206,
					-5.555521647135379
				],
				[
					-130.55552164713538,
					2.7778116861979925
				],
				[
					-109.72218831380201,
					5.555572509765625
				],
				[
					-83.33333333333326,
					4.1666666666667425
				],
				[
					-76.38885498046875,
					4.1666666666667425
				],
				[
					-62.5,
					0
				],
				[
					-59.72218831380201,
					-2.7777608235676325
				],
				[
					-58.33333333333326,
					-4.166666666666629
				],
				[
					-56.944427490234375,
					-6.944427490234375
				],
				[
					-56.944427490234375,
					-8.333333333333258
				],
				[
					-66.66666666666663,
					-13.88885498046875
				],
				[
					-104.16666666666663,
					-20.833333333333258
				],
				[
					-125,
					-20.833333333333258
				],
				[
					-141.66666666666663,
					-18.05552164713538
				],
				[
					-162.49999999999994,
					-12.5
				],
				[
					-168.05552164713538,
					-9.722188313802008
				],
				[
					-172.22218831380206,
					-6.944427490234375
				],
				[
					-174.99999999999994,
					-4.166666666666629
				],
				[
					-176.3888549804687,
					-4.166666666666629
				],
				[
					-172.22218831380206,
					1.3889058430989962
				],
				[
					-151.3888549804687,
					9.722239176432367
				],
				[
					-106.94442749023438,
					18.055572509765625
				],
				[
					-90.27776082356763,
					18.055572509765625
				],
				[
					-70.83333333333326,
					16.666666666666742
				],
				[
					-62.5,
					13.888905843098996
				],
				[
					-61.111094156901004,
					13.888905843098996
				],
				[
					-59.72218831380201,
					12.5
				],
				[
					-73.611094156901,
					4.1666666666667425
				],
				[
					-91.66666666666663,
					-2.7777608235676325
				],
				[
					-108.33333333333326,
					-8.333333333333258
				],
				[
					-122.22218831380201,
					-11.111094156901004
				],
				[
					-131.94442749023432,
					-11.111094156901004
				],
				[
					-149.99999999999994,
					-8.333333333333258
				],
				[
					-156.94442749023432,
					-5.555521647135379
				],
				[
					-161.111094156901,
					-2.7777608235676325
				],
				[
					-165.2777608235677,
					-1.38885498046875
				],
				[
					-166.66666666666663,
					0
				],
				[
					-168.05552164713538,
					0
				],
				[
					-169.44442749023432,
					1.3889058430989962
				],
				[
					-169.44442749023432,
					1.3889058430989962
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 3,
			"versionNonce": 2012278288,
			"isDeleted": false,
			"id": "cXZdXBlYhyDno7LzFKutl",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 505.6232472443794,
			"y": 779.7725057626642,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 1142273776,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623752039,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 3,
			"versionNonce": 1534650384,
			"isDeleted": false,
			"id": "We-y0NW3jYoiLMpZkw72k",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 497.28988847973096,
			"y": 656.4557483313686,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 158588144,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623755846,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "ellipse",
			"version": 73,
			"versionNonce": 15094512,
			"isDeleted": false,
			"id": "jakRHMlCrWr6ASKxcv5kP",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -144.3767527556206,
			"y": 1073.8648548445353,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 379.16664123535156,
			"height": 370.8332824707031,
			"seed": 1367065328,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714623815278,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 91,
			"versionNonce": 1091581968,
			"isDeleted": false,
			"id": "8SvqNeWq",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -58.316153179277535,
			"y": 1153.714260035212,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 80.12443542480469,
			"height": 71.40359196253925,
			"seed": 946262032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623850377,
			"link": null,
			"locked": false,
			"fontSize": 57.1228735700314,
			"fontFamily": 1,
			"text": "TL",
			"rawText": "TL",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "TL",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 42,
			"versionNonce": 1586446576,
			"isDeleted": false,
			"id": "RilH81OR",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 87.6405728949411,
			"y": 1162.2012489093722,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 59.27995300292969,
			"height": 50.000000000000085,
			"seed": 249714928,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623853558,
			"link": null,
			"locked": false,
			"fontSize": 40.00000000000007,
			"fontFamily": 1,
			"text": "TR",
			"rawText": "TR",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "TR",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 42,
			"versionNonce": 1982932720,
			"isDeleted": false,
			"id": "DRlk3Ano",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -50.21945823298847,
			"y": 1262.9227246857467,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 68.16455078125,
			"height": 64.27852422362537,
			"seed": 134720016,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623845731,
			"link": null,
			"locked": false,
			"fontSize": 51.42281937890029,
			"fontFamily": 1,
			"text": "BL",
			"rawText": "BL",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "BL",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 44,
			"versionNonce": 802820624,
			"isDeleted": false,
			"id": "mnEb0JZt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 97.6138668606236,
			"y": 1265.1178901447238,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 51.50187683105469,
			"height": 45.833358764648445,
			"seed": 1872544496,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714623859668,
			"link": null,
			"locked": false,
			"fontSize": 36.66668701171876,
			"fontFamily": 1,
			"text": "BR",
			"rawText": "BR",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "BR",
			"lineHeight": 1.25
		},
		{
			"type": "line",
			"version": 115,
			"versionNonce": 1167436816,
			"isDeleted": false,
			"id": "I3gMpTbPSol90l4vrIsMZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 55.850526203046684,
			"y": 1074.7012489093722,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 12.5,
			"height": 375,
			"seed": 1331394800,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714623869162,
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
					-12.5,
					375
				]
			]
		},
		{
			"type": "line",
			"version": 38,
			"versionNonce": 833953808,
			"isDeleted": false,
			"id": "FTPs0aparEcDzez7q9xeB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 235.01716743839825,
			"y": 1237.2012489093722,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 379.16664123535156,
			"height": 4.1666412353515625,
			"seed": 1911406320,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714623879326,
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
					-379.16664123535156,
					4.1666412353515625
				]
			]
		},
		{
			"type": "rectangle",
			"version": 762,
			"versionNonce": 614978288,
			"isDeleted": false,
			"id": "2EWNZ8wHzcwEDFdb3flku",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 12.59978186823156,
			"x": -457.6301075963312,
			"y": 242.79924270437922,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 196.20335970473667,
			"height": 163.72831368177367,
			"seed": 617662704,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "kKRlmvFLP8opz5FANN0YO",
					"type": "arrow"
				}
			],
			"updated": 1714624357978,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 730,
			"versionNonce": 1758073360,
			"isDeleted": false,
			"id": "zVB6YBxS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 12.59978186823156,
			"x": -406.28179802258006,
			"y": 310.24666902689097,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 78.86160278320312,
			"height": 37.056902181483906,
			"seed": 329919216,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714624357978,
			"link": null,
			"locked": false,
			"fontSize": 29.645521745187125,
			"fontFamily": 1,
			"text": "Servo",
			"rawText": "Servo",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Servo",
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 2177,
			"versionNonce": 1037618704,
			"isDeleted": false,
			"id": "kKRlmvFLP8opz5FANN0YO",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 15.70682231516981,
			"x": -481.4289705109362,
			"y": 232.7787065395945,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 248.60946145133752,
			"height": 35.239876168718666,
			"seed": 1694977264,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714624359143,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "2EWNZ8wHzcwEDFdb3flku",
				"focus": 0.7936960966266872,
				"gap": 27.99796614058006
			},
			"endBinding": {
				"elementId": "2EWNZ8wHzcwEDFdb3flku",
				"gap": 25.145475642298365,
				"focus": -0.820711762562363
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					127.67346806230572,
					-23.85388452707309
				],
				[
					248.60946145133752,
					11.385991641645578
				]
			]
		},
		{
			"type": "rectangle",
			"version": 847,
			"versionNonce": 247687920,
			"isDeleted": false,
			"id": "0fej8uMCYviYZZyN9OjeC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 17.281690082274118,
			"x": -470.60610296623827,
			"y": 507.89446366969497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 196.20335970473667,
			"height": 163.72831368177367,
			"seed": 1649909264,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1714624389727,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 814,
			"versionNonce": 1838104304,
			"isDeleted": false,
			"id": "I0zqIgVf",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 17.281690082274118,
			"x": -407.6304311983466,
			"y": 578.3966937820493,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 78.86160278320312,
			"height": 37.056902181483906,
			"seed": 1608080400,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714624378110,
			"link": null,
			"locked": false,
			"fontSize": 29.645521745187125,
			"fontFamily": 1,
			"text": "Servo",
			"rawText": "Servo",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Servo",
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 2449,
			"versionNonce": 1506813456,
			"isDeleted": false,
			"id": "Ykb0_e7qZMpoNfkK4fwFa",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 4.686868474757675,
			"x": -630.6585793448868,
			"y": 597.9574899454483,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 248.60946145133752,
			"height": 35.239876168718666,
			"seed": 41114128,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1714624394928,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					127.67346806230572,
					-23.85388452707309
				],
				[
					248.60946145133752,
					11.385991641645578
				]
			]
		},
		{
			"type": "text",
			"version": 21,
			"versionNonce": 7370768,
			"isDeleted": false,
			"id": "pCiLTmNr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -577.591605651626,
			"y": 648.4858281062875,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 143.85984802246094,
			"height": 25,
			"seed": 1646855920,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714624410609,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Ant Clcok Wise",
			"rawText": "Ant Clcok Wise",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Ant Clcok Wise",
			"lineHeight": 1.25
		},
		{
			"id": "vh1ojUakEBa_-rHcxss0n",
			"type": "ellipse",
			"x": 662.6121919992086,
			"y": 1413.7537136986355,
			"width": 232.13012695312455,
			"height": 203.43976702008922,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1859093325,
			"version": 827,
			"versionNonce": 1549742605,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1714681821979,
			"link": null,
			"locked": false
		},
		{
			"id": "Ys0dtD-1ypU82FtDqlKE9",
			"type": "rectangle",
			"x": -101.59121201864878,
			"y": 1964.0845242455105,
			"width": 461.65196010044633,
			"height": 339.06633649553555,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 814179629,
			"version": 55,
			"versionNonce": 1071247725,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1714681759124,
			"link": null,
			"locked": false
		},
		{
			"id": "ue3R5WzoBlO6dZiOcwGJu",
			"type": "line",
			"x": -93.76650498739878,
			"y": 1969.3009374709568,
			"width": 461.6517857142858,
			"height": 271.25313895089266,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 332610509,
			"version": 111,
			"versionNonce": 1651272355,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1714681768169,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					224.305419921875,
					-271.25313895089266
				],
				[
					461.6517857142858,
					-2.608206612723052
				],
				[
					451.2189592633929,
					-5.216413225446331
				]
			],
			"lastCommittedPoint": [
				451.2189592633929,
				-5.216413225446331
			],
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null
		},
		{
			"id": "gAFdqbhbftOPD6qAdtvda",
			"type": "arrow",
			"x": 829.5370664411728,
			"y": 1528.5146738688363,
			"width": 285.09095709190296,
			"height": 605.103018624442,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1986138371,
			"version": 109,
			"versionNonce": 1264361603,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1714681792470,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					285.09095709190296,
					203.94434345798254
				],
				[
					250.38748604910688,
					605.103018624442
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1971c2",
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
		"scrollX": 2726.995527156519,
		"scrollY": 505.92795708064887,
		"zoom": {
			"value": 0.2
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