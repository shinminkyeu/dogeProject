pragma solidity >=0.4.0 <0.6.0;

import "./DogContract.sol";

contract DogApp is DogContract {
    //부모견의 소유주에게 메시지를 보내기 위한 이벤트
    event approveRegisterParent(uint _dogId, uint _pDogId, address _from, address _to);

    function registerDog(uint32 _birth, KIND _kind, bool _gender, bool _alive, string memory _regiNo,
     string memory _rfid, uint _fatherId, uint _motherId ) public {
        //_fatherId 또는 _motherId 는 내용이 없다면 0이다.
        uint age = now - _birth;
        uint momId = _motherId;
        uint dadId = _fatherId;
        require(dogs[dadId].birth > _birth, "아빠견이 자식견보다 어립니다.");   //부모견의 나이가 자식견보다 나이가 크지 않다면
        require(dogs[momId].birth > _birth, "엄마견이 자식견보다 어립니다.");   //부모견의 나이가 자식견보다 나이가 크지 않다면
        if(age < ageRestriction) {      //성견인지 아닌지 확인(6개월.)
            require(_motherId != 0, "Register it's mother dog");     //나이가 어리다면, 부모에 대한 id값이 있는지 확인하고 없다면 error를 발생시킨다.
            require(dogs[momId].gender, "It's not female");          //입력된 어미견의 성별이 암컷이 아니라면.
            require(_currentDogOwner(_motherId) == msg.sender, "mother dog is not yours"); //부모견이 나의 개가 아니라면 error 발생
        }
        uint dogId = _newDog(_birth, _kind, _gender, _alive, _regiNo, _rfid);
        if(_currentDogOwner(_motherId) != msg.sender) {
            momId = 0;
            emit approveRegisterParent(dogId, _motherId, msg.sender, _currentDogOwner(_motherId));
        }
        if(_currentDogOwner(_fatherId) != msg.sender) {
            dadId = 0;
            emit approveRegisterParent(dogId, _fatherId, msg.sender, _currentDogOwner(_fatherId));
        }
        _registerParents(dogId, dadId, momId);
    }
    //성견등록자가 다른 소유의 견을 부모로 등록할때 메시지를 보내고, 승인을 받으면, 이 함수 실행.
    function registerParents(uint _dogId, uint _pDogId, address _pDogOwner) public onlyDogOwner(_dogId){
        require(_pDogOwner == _currentDogOwner(_pDogId), "The dog is not his");
        Dog memory pDog = dogs[_pDogId];
        if(pDog.gender) //true == 암컷, false == 수컷
            _registerParents(_dogId, 0, _pDogId);
        else
            _registerParents(_dogId, _pDogId, 0);
    }
    //자신의 개에 대한 새끼견 등록 //필요 없는듯?
    function registerChildren(uint _dogId, uint[] memory _children) public onlyDogOwner(_dogId){
        //다른 사람이 해도 자식 추가가 되는듯 하다.
        require(dogs[_dogId].gender, "Your dog must be female");
        for(uint i = 0 ; i < _children.length; i++) {
            parentToChildren[_dogId].push(_children[i]);
        }
    }
    function distributeDog(uint _dogId, address _to) public onlyDogOwner(_dogId) {
        //개의 소유주 변경 시.
        //1. msg.sender의 개를 뺀다.
        //2. _to에게 새로운 개를 추가한다.
        //3. _dogId address List 에 따른 주인을 추가한다.
        ownerToDogCount[msg.sender]--;
        ownerToDogCount[_to]++;
        dogToOwner[_dogId].push(_to);
    }
    function stateChangeDog(uint _dogId, bool _alive) public onlyDogOwner(_dogId) {
        dogs[_dogId].alive = _alive;
    }
    function addRegisterNumber(uint _dogId, string memory _registerNo) public onlyDogOwner(_dogId){
        dogs[_dogId].registrationNumber = _registerNo;
    }
    function addRFID(uint _dogId, string memory _rfid) public onlyDogOwner(_dogId){
        dogs[_dogId].rfid = _rfid;
    }
}