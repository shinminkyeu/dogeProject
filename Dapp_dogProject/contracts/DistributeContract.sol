pragma solidity >=0.4.21 <0.6.0;

import "./DogApp.sol";

contract DistributeContract is DogApp {
    enum STATE {WAITTING, READY, COMPLETION}
    struct Trade{
        uint32 dogId;
        uint8 price;
        STATE state;
        address owner;
        address buyer;
        string region;
    }
    Trade[] trade;
    mapping(uint => uint[]) dogTrade;       //강아지 id => 거래 id : 강아지가 어느 거래에 포함되었는지
    mapping(address => uint[]) ownerTrade;  //분양자 id => 거래 id : 분양자가 어느 거래에 포함되었는지
    mapping(address => uint[]) buyerTrade;  //구매자 id => 거래 id : 구매자가 어느 거래에 포함되었는지
    address temp;                           //가짜 주소.
    modifier onlyTradeOwner(uint _tradeid) {
        require(trade[_tradeid].owner == msg.sender, "You are not owner of this trade");
        _;
    }
    function showTrade(uint _tradeId) public view returns(uint32, uint8, STATE, address, address, string memory) {
        return(trade[_tradeId].dogId, trade[_tradeId].price, trade[_tradeId].state,trade[_tradeId].owner,
         trade[_tradeId].buyer, trade[_tradeId].region);
    }

    //분양을 원하는 사람이 거래를 등록한다.
    //무슨 강아지를, 얼마에, 누가, 거래지역
    function resisterTrade(uint32 _dogId, uint8 _price, address _owner, string memory _region) public onlyDogOwner(_dogId) returns(uint)  {
        uint id = trade.push(Trade(_dogId, _price, STATE.WAITTING, _owner, temp, _region))-1;
        return id;
    }
    //분양을 희망하는 사람이 거래를 예약한다.
    //이전에는 분양 대기중인 상태여야 하며, 예약을 희망하는 사람은 가격 이상의 가치를 지갑에 소유해야 한다.
    //원하는 거래 id, 구매자 지갑주소.
    function reserveTrade(uint _tradeId, address _buyer) public {
        require(trade[_tradeId].state == STATE.WAITTING, "분양중인 상태가 아닙니다.");     //대기 상태인 거래만 구매자를 받을 수 있다.
        require(_buyer.balance >= trade[_tradeId].price, "상대방의 잔액이 부족합니다.");
        trade[_tradeId].state = STATE.READY;
        trade[_tradeId].buyer = _buyer;
    }
    //거래를 완료하는 함수.
    function completeTrade(uint _tradeId) public onlyTradeOwner(_tradeId){
        require(trade[_tradeId].state == STATE.READY, "예약상태가 아닙니다.");
        trade[_tradeId].state = STATE.COMPLETION;
        distributeDog(trade[_tradeId].dogId, trade[_tradeId].buyer);
    }
    //거래 취소하는 함수.
    function cancleTrade(uint _tradeId) public {
        require(trade[_tradeId].state == STATE.READY, "예약상태가 아닙니다.");
        trade[_tradeId].state = STATE.WAITTING;
        trade[_tradeId].buyer = temp;
    }
}