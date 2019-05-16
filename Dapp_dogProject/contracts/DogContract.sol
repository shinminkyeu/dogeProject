pragma solidity >=0.4.0 <0.6.0;

contract DogContract {
    enum KIND {CHIWAWA, POODLE}
    struct Dog {
        uint32 birth;   // 유닉스타임 (년월일까지만 00시00분00초)
        KIND kind;      // enum 으로 인한 종류 설정.(DB와 맞춰야함.)
        bool gender;    // true = 여자, false = 남자
        bool alive;     // true = 생존, false = 죽음
        string registrationNumber;            //동물보호관리시스템 등록번호
        string rfid;                           //동물보호관리시스템 RFID
    }
    event newDog(uint _dogId, address _owner);  //개가 등록돼면 발생
    event registeredParent(string _message, uint _dogId, uint _pDogId);

    Dog[] dogs;
    mapping(uint => uint[2]) childToParent;     // 새끼개로 부모개 읽어오기, 0=>어미견, 1=부모견
    mapping(uint => uint[]) parentToChildren;   // 부모개로 새끼개 읽어오기
    mapping(uint => address[]) dogToOwner;      // dogId로 주인 지갑 주소 가져오기
    mapping(address => uint) ownerToDogCount; // 지갑 주소에 따른 개id 가져오기
    uint ageRestriction = 6 * 30 * 24 * 3600;   // 성견기준 6개월을 초 단위로.

    modifier onlyDogOwner(uint _dogId) {
        require(msg.sender == _currentDogOwner(_dogId), "You are not owner of this dog");
        _;
    }

    function _currentDogOwner(uint _dogId) internal view returns(address){
        uint _currentOwner = dogToOwner[_dogId].length - 1;      //가장 최근index == 현재 견주.
        return dogToOwner[_dogId][_currentOwner];
    }

    function _newDog(uint32 _birth, KIND _kind, bool _gender, bool _alive, string memory _regiNo, string memory _rfid) internal returns(uint) {
        uint id = dogs.push(Dog(_birth, _kind, _gender, _alive, _regiNo, _rfid)) - 1;
        ownerToDogCount[msg.sender]++;
        dogToOwner[id].push(msg.sender);
        emit newDog(id, msg.sender);
        return id;
    }

    function _registerParents(uint _dogId, uint _maleId, uint _femaleId) internal onlyDogOwner(_dogId){
        //부모견에 대한 정보가 있다면 수정하지 않는다.(한번 등록된 부모견 정보 수정 불가.) // 0 == default
        if(childToParent[_dogId][0] == 0) {
            childToParent[_dogId][0] = _femaleId;
            parentToChildren[_femaleId].push(_dogId);
            emit registeredParent("Mom Dog Registered!", _dogId, _femaleId);
        }
        if(childToParent[_dogId][1] == 0) {
            childToParent[_dogId][1] = _maleId;
            parentToChildren[_maleId].push(_dogId);
            emit registeredParent("Dad Dog Registered!", _dogId, _maleId);
        }
    }

    function findDog(uint _dogId) public view returns(uint32, KIND, bool, bool){
        Dog memory result = dogs[_dogId];
        return (result.birth, result.kind, result.gender, result.alive);
    }

    function showDogToOwner(uint _dogId) external view returns(uint, KIND, bool, bool) {
        Dog memory result = dogs[_dogId];
        return(result.birth, result.kind, result.gender, result.alive);
    }

    function showOwnerToDog(address _user) external view returns(uint[] memory) {
        uint[] memory result = new uint[](ownerToDogCount[_user]);
        uint index = 0;
        for(uint dogId = 0 ; dogId < dogs.length ; dogId++) {
            if(_currentDogOwner(dogId) == _user) {
                result[index++] = dogId;
            }
        }
        return result;
    }

    function showChildToParent(uint _dogId) external view returns(uint[2] memory) {
        return childToParent[_dogId];
    }

    function showParentToChildren(uint _dogId) external view returns(uint[] memory) {
        return parentToChildren[_dogId];
    }
}