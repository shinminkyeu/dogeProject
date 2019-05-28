let contract;
const contractAddress = "0xfd220453e84762842bae8f1ed64e50dcf2141d7d";
let doge_ABI = [
	{
		"constant": true,
		"inputs": [
			{
				"name": "message",
				"type": "bytes"
			},
			{
				"name": "r",
				"type": "bytes32"
			},
			{
				"name": "s",
				"type": "bytes32"
			},
			{
				"name": "v",
				"type": "uint8"
			}
		],
		"name": "checkSignature",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "pure",
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
		"name": "cancelTrade",
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
		"inputs": [],
		"name": "showWattingTrade",
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
				"name": "_dogId",
				"type": "uint32"
			},
			{
				"name": "_price",
				"type": "uint8"
			},
			{
				"name": "_region",
				"type": "string"
			}
		],
		"name": "registerTrade",
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
		"constant": false,
		"inputs": [],
		"name": "setDogs",
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
		"constant": true,
		"inputs": [
			{
				"name": "message",
				"type": "bytes"
			}
		],
		"name": "doHash",
		"outputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "pure",
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
				"name": "dogId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "pDogId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "to",
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
				"name": "dogId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "owner",
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
				"name": "message",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "dogId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "pDogId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "owner",
				"type": "address"
			}
		],
		"name": "registeredParent",
		"type": "event"
	}
];
const sigParams = [
    {
        type: 'string',
        name: 'message',
        value: '지갑을 인증해 주세요.\nPlease verify your wallet.'
    }];
$(document).ready(async () => {
    if (ethereum) { // 최신 메타마스크라면,
        const web3 = new Web3(ethereum);
        try { // 권한 요청이 필요
            await ethereum.enable();
        } catch (err) {
            // 권한 요청 거부시 코드
        }
    } else if (typeof web3 !== 'undefined') { // 구버전 메타마스크라면
        web3 = new Web3(web3.currentProvider); // 권한 요청 없이 실행
    } else {
        // 메타마스크가 없으면 실행될 코드
    }
    // contract 객체 할당
    contract = web3.eth.contract(doge_ABI).at(contractAddress);
    $('#doge-home').attr('href', location.hostname)
    if (location.href == location.hostname + '/user') {
        $('#doge-user').text('Logout')
            .attr('href', location.hostname + '/logout')
    } else {
        $('<form name="account" method="post"></form>')
            .attr('action', location.hostname + '/user')
            .append('<input type="hidden" name="account" value=' + web3.eth.accounts[0] + '>')
            .insertAfter('#doge-user');
        $('#doge-user').text('User')
            .attr('href', '#;')
            .click(document.account.submit());
    }
});
function reg_dog(_birth, _kind, _gender, _alive, _regiNo, _rfid, _dadId, _momId, _inputId) {
    let birth = (new Date(_birth).getTime() / 1000) - (3600 * 9)
    contract.registerDog.sendTransaction(birth,_kind,_gender,_alive, _regiNo, _rfid, _dadId, _momId,
         (err, res) => {
            if (err) console.log(err);
            contract.newDog({}, (err2, eve) => {
                if (err2) console.log(err2);
                if (eve.args.owner === web3.eth.accounts[0]) {
                    find_dog(eve.args.dogId.toNumber());
                    $('#'+_inputId).val = eve.args.dogId.toNumber();
                }
            });
        }
    );
}
/*
function find_dog(id) {
    contract.findDog.call(id, (err, res) => {
        if (err) console.log(err)
        let birth = new Date(res[0].toNumber() * 1000)
        $('#dog').html('<ul>' +
            '<li>개 생일 : ' + birth + '</li>' +
            '<li>개 품종 : ' + res[1].toNumber() + '</li>' +
            '<li>개 성별 : ' + (res[2] ? '암컷' : '수컷') + '</li>' +
            '<li>생존 여부 : ' + res[3].toString() + '</li>' +
            '<li>등록 번호 : ' + res[4] + '</li>' +
            '<li>RFID : ' + res[5] + '</li></ul>')
    })
}
//*/
/*
function signMsg() {
    let from = web3.eth.accounts[0];
    $('input[name=from]').val(from);
    $('input[name=data]').val(JSON.stringify(sigParams))
    web3.currentProvider.sendAsync({
        method: 'eth_signTypedData',
        params: [sigParams, from],
        from: from,
    }, function (err, res) {
        if (err) return console.error(err)
        console.log(res.result);
        $('input[name=sigRes]').val(res.result);
        document.signData.submit();
    })
}

//*/