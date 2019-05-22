const doge_ABI = [
	{
		"constant": false,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"name": "_pDogId",
				"type": "uint256"
			},
			{
				"name": "_pDogOwner",
				"type": "address"
			}
		],
		"name": "registerParents",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"name": "_alive",
				"type": "bool"
			}
		],
		"name": "stateChangeDog",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"name": "_to",
				"type": "address"
			}
		],
		"name": "distributeDog",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_user",
				"type": "address"
			}
		],
		"name": "showOwnerToDog",
		"outputs": [
			{
				"name": "",
				"type": "uint256[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint32"
			},
			{
				"name": "_price",
				"type": "uint8"
			},
			{
				"name": "_owner",
				"type": "address"
			},
			{
				"name": "_region",
				"type": "string"
			}
		],
		"name": "resisterTrade",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_value",
				"type": "uint8"
			}
		],
		"name": "changeKindCount",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_tradeId",
				"type": "uint256"
			}
		],
		"name": "cancleTrade",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			}
		],
		"name": "showParentToChildren",
		"outputs": [
			{
				"name": "",
				"type": "uint256[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			}
		],
		"name": "findDog",
		"outputs": [
			{
				"name": "",
				"type": "uint32"
			},
			{
				"name": "",
				"type": "uint8"
			},
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_tradeId",
				"type": "uint256"
			},
			{
				"name": "_buyer",
				"type": "address"
			}
		],
		"name": "reserveTrade",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"name": "_children",
				"type": "uint256[]"
			}
		],
		"name": "registerChildren",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_tradeId",
				"type": "uint256"
			}
		],
		"name": "showTrade",
		"outputs": [
			{
				"name": "",
				"type": "uint32"
			},
			{
				"name": "",
				"type": "uint8"
			},
			{
				"name": "",
				"type": "uint8"
			},
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_tradeId",
				"type": "uint256"
			}
		],
		"name": "completeTrade",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_birth",
				"type": "uint32"
			},
			{
				"name": "_kind",
				"type": "uint8"
			},
			{
				"name": "_gender",
				"type": "bool"
			},
			{
				"name": "_alive",
				"type": "bool"
			},
			{
				"name": "_regiNo",
				"type": "string"
			},
			{
				"name": "_rfid",
				"type": "string"
			},
			{
				"name": "_fatherId",
				"type": "uint256"
			},
			{
				"name": "_motherId",
				"type": "uint256"
			}
		],
		"name": "registerDog",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"name": "_rfid",
				"type": "string"
			}
		],
		"name": "addRFID",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			}
		],
		"name": "showDogToOwner",
		"outputs": [
			{
				"name": "",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			}
		],
		"name": "showChildToParent",
		"outputs": [
			{
				"name": "",
				"type": "uint256[2]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"name": "_registerNo",
				"type": "string"
			}
		],
		"name": "addRegisterNumber",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "_pDogId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_to",
				"type": "address"
			}
		],
		"name": "approveRegisterParent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "_owner",
				"type": "address"
			}
		],
		"name": "newDog",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_message",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "_dogId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "_pDogId",
				"type": "uint256"
			}
		],
		"name": "registeredParent",
		"type": "event"
	}
]