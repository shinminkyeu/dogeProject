pragma solidity >=0.4.21 <0.6.0;

contract DistributeContract {
    enum STATE {WATTING, READY, COMPLETION}
    struct Trade{
        uint32 dogId;
        uint8 price;
        STATE state;
        address owner;
        address buyer;
    }
    Trade[] trade;
    mapping(uint => uint[]) dogTrade;       //강아지 id => 거래 id : 강아지가 어느 거래에 포함되었는지
    mapping(address => uint[]) ownerTrade;  //분양자 id => 거래 id : 분양자가 어느 거래에 포함되었는지
    mapping(address => uint[]) buyerTrade;  //구매자 id => 거래 id : 구매자가 어느 거래에 포함되었는지
    address temp;                           //가짜 주소.
    modifier onlyOwner(uint id) {
        assert(id == 1);
        _;
    }
    //분양을 원하는 사람이 거래를 등록한다.
    //무슨 강아지를, 얼마에, 누가
    function resisterTrade(uint32 _dogId, uint8 _price, address _owner) public returns(uint) {
        assert(true);
        uint id = trade.push(Trade(_dogId, _price, STATE.WATTING, _owner, temp))-1;
        return id;
    }
    //분양을 희망하는 사람이 거래를 예약한다.
    //이전에는 분양 대기중인 상태여야 하며, 예약을 희망하는 사람은 가격 이상의 가치를 지갑에 소유해야 한다.
    //원하는 거래 id, 구매자 지갑주소.
    function reserveTrade(uint _tradeId, address _buyer) public {
        assert(trade[_tradeId].state == STATE.WATTING);
        assert(_buyer.balance >= trade[_tradeId].price);
        trade[_tradeId].state = STATE.READY;
        trade[_tradeId].buyer = _buyer;
    }
    //거래를 완료하는 함수.
    function completeTrade(uint _tradeId) public {
        trade[_tradeId].state = STATE.COMPLETION;
    }
}