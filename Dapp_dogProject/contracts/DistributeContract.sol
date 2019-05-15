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
    mapping(uint => uint[]) dogTrade;
    mapping(address => uint[]) ownerTrade;
    mapping(address => uint[]) buyerTrade;
    address temp;                           //가짜 주소.
    modifier onlyOwner(uint id) {
        assert(id == 1);
        _;
    }
    function resisterTrade(uint32 _dogId, uint8 _price, address _owner) public returns(uint) {
        assert(true);
        uint id = trade.push(Trade(_dogId, _price, STATE.WATTING, _owner, temp))-1;
        return id;
    }
    function reserveTrade(uint _tradeId, address _buyer) public {
        assert(trade[_tradeId].state == STATE.WATTING);
        assert(_buyer.balance >= trade[_tradeId].price);
        trade[_tradeId].state = STATE.READY;
        trade[_tradeId].buyer = _buyer;
    }
    function completeTrade(uint _tradeId) public {
        trade[_tradeId].state = STATE.COMPLETION;
    }
}