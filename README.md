<script>

// 그리디 알고리즘
var greedy_data = [
  ['순번', '문제 번호', '문제 이름', '난이도', '풀이 링크'],
  ['', '1343', '폴리오미노', '6', ''],
  ['', '14916', '거스름돈', '6', ''],
  ['', '2217', '로프', '7', ''],
  ['', '13305', '주유소', '7', ''],
  ['', '1758', '알바생 강호', '7', ''],
  ['', '11508', '2+1 세일', '7', ''],
  ['', '11399', 'ATM', '7', ''],
  ['', '11047', '동전 0', '7', ''],
  ['', '20115', '에너지 드링크', '8', ''],
  ['', '20300', '서강근육맨', '8', ''],
  ['', '1541', '잃어버린 괄호', '9', ''],
  ['', '20365', '블로그2', '9', ''],
  ['', '16953', 'A → B', '9', ''],
  ['', '21314', '민겸 수', '9', ''],
  ['', '1080', '꿀 따기', '10', ''],
  ['', '1931', '회의실 배정', '10', ''],
  ['', '21758', '행렬', '10', ''],
  ['', '11000', '강의실 배정', '11', ''],
  ['', '13164', '행복 유치원', '11', ''],
  ['', '19598', '최소 회의실 개수', '11', ''],
  ['', '2212', '센서', '11', ''],
  ['', '1092', '배', '11', ''],
  ['', '2141', '우체국', '12', ''],
  ['', '13975', '파일 합치기 3', '12', ''],
  ['', '1715', '카드 정렬하기', '12', ''],
  ['', '2285', '우체국', '12', ''],
  ['', '2812', '크게 만들기', '13', ''],
  ['', '8980', '택배', '14', ''],
];

var bruteforce_data = [
  ['순번', '문제 번호', '문제 이름', '난이도', '풀이 링크'],
  ['', '2231', '분해합', '4', ''],
  ['', '2309', '일곱 난쟁이', '5', ''],
  ['', '10448', '유레카 이론', '5', ''],
  ['', '1018', '체스판 다시 칠하기', '7', ''],
  ['', '3085', '사탕 게임', '8', ''],
  ['', '2503', '숫자 야구', '8', ''],
  ['', '1912', '연속합', '9', ''],
  ['', '1182', '부분수열의 합', '9', ''],
];

var dfs_data = [
  ['순번', '문제 번호', '문제 이름', '난이도', '풀이 링크'],
  ['', '1012', '유기농 배추', '9', ''],
  ['', '11724', '연결 요소의 개수', '9', ''],
  ['', '10552', 'DOM', '9', ''],
  ['', '11403', '경로 찾기', '10', ''],
  ['', '2468', '안전 영역', '10', ''],
  ['', '1743', '음식물 피하기', '10', ''],
  ['', '2667', '단지번호붙이기', '10', ''],
  ['', '2583', '영역 구하기', '10', ''],
  ['', '10026', '적록색약', '11', ''],
  ['', '9466', '텀 프로젝트', '13', ''],
  ['', '10265', 'MT', '17', ''],
];

var data = [];
data[0] = greedy_data;
data[1] = bruteforce_data;
data[2] = dfs_data;

window.onload = function(){
  var greedy = document.getElementById ('greedy');
  var dfs = document.getElementById ('dfs');

  var name = [];
  name[0] = greedy;
  name[1] = bruteforce;
  name[2] = dfs;

  for (var n=0; n<data.length; n++){
    var table = document.createElement('table');

    name[n].appendChild(table);

    // 테이블 헤드
    var thead = document.createElement('thead');
    table.appendChild(thead);

    var tr = document.createElement('tr');
    thead.appendChild(tr);

    for (var i=0; i<data[n][0].length; i++){
        var th = document.createElement('th');
        tr.appendChild(th);
        th.innerHTML = data[n][0][i];
    }

    //테이블 바디
    var tbody = document.createElement('tbody');
    table.appendChild(tbody);

    for (var i=1; i<data[n].length; i++){
        var tr = document.createElement('tr');
        tbody.appendChild(tr);

        var num = `${i}`;
        if(num.length <= 1){
          num = `0${i}`
        }
        var td = document.createElement('td');
        tr.appendChild(td);
        td.innerHTML = num;

        var url = `<a href="https://www.acmicpc.net/problem/${data[n][i][1]}" target="_blank" rel="noopener noreferrer">`;
        url += `${data[n][i][1]}`;
        url += '</a>';
        var td = document.createElement('td');
        tr.appendChild(td);
        td.innerHTML = url;


        var url = `<a href="https://www.acmicpc.net/problem/${data[n][i][1]}" target="_blank" rel="noopener noreferrer">`;
        url += `${data[n][i][2]}`;
        url += '</a>';
        var td = document.createElement('td');
        tr.appendChild(td);
        td.innerHTML = url;

        var url = `<img height="25px" width="25px" src="https://static.solved.ac/tier_small/${data[n][i][3]}.svg">`
        var td = document.createElement('td');
        tr.appendChild(td);
        td.innerHTML = url;

        var td = document.createElement('td');
        tr.appendChild(td);
        td.innerHTML = `${data[n][i][4]}`;

        if(data[n][i][3] <= 5){
          randomlinks_bronze.push(`${data[n][i][1]}`);
        }else if (data[n][i][3] <= 10) {
          randomlinks_silver.push(`${data[n][i][1]}`);
        } else if (data[n][i][3] <= 15) {
          randomlinks_gold.push(`${data[n][i][1]}`);
        } else if (data[n][i][3] <= 20) {
          randomlinks_platinum.push(`${data[n][i][1]}`);
        } else if (data[n][i][3] <= 25) {
          randomlinks_diamond.push(`${data[n][i][1]}`);
        }
        randomlinks_all.push(`${data[n][i][1]}`);
    }
  }
}

// 깊이 우선 탐색 알고리즘
  var randomlinks_all=new Array()
  var randomlinks_bronze=new Array()
  var randomlinks_silver=new Array()
  var randomlinks_gold=new Array()
  var randomlinks_platinum=new Array()
  var randomlinks_diamond=new Array()

  function randomlink_all(){
    window.open('about:_blank').window.location= 'https://www.acmicpc.net/problem/' + randomlinks_all[Math.floor(Math.random()*randomlinks_all.length)]
  }
  function randomlink_bronze(){
    window.open('about:_blank').window.location= 'https://www.acmicpc.net/problem/' + randomlinks_bronze[Math.floor(Math.random()*randomlinks_bronze.length)]
  }
  function randomlink_silver(){
    window.open('about:_blank').window.location= 'https://www.acmicpc.net/problem/' + randomlinks_silver[Math.floor(Math.random()*randomlinks_silver.length)]
  }
  function randomlink_gold(){
    window.open('about:_blank').window.location= 'https://www.acmicpc.net/problem/' + randomlinks_gold[Math.floor(Math.random()*randomlinks_gold.length)]
  }
  function randomlink_platinum(){
    window.open('about:_blank').window.location= 'https://www.acmicpc.net/problem/' + randomlinks_platinum[Math.floor(Math.random()*randomlinks_platinum.length)]
  }
  function randomlink_diamond(){
    window.open('about:_blank').window.location= 'https://www.acmicpc.net/problem/' + randomlinks_diamond[Math.floor(Math.random()*randomlinks_diamond.length)]
  }


</script>

# 코딩 테스트 대비 백준 문제 추천

백준(BOJ)에 정말 많은 문제들이 있기에 그중에 괜찮은 문제들만 선별해 보았다.  
<br/>
알고리즘 유형에 따라 나눠봤지만 실제 코딩 테스트에서는 어떤 알고리즘으로 풀어야 하는지도 생각을 해야 한다. 그렇기 때문에 문제를 풀 때도 **어떤 방식으로 해결할지 결정하고, 사용할 알고리즘과 자료구조를 선택해야 하기 때문에** 아래 문제들 중 랜덤으로 풀 수 있는 기능을 만들어 봤다.  
<br/>
<a href="javascript:randomlink_all()">무작위 풀어보기</a>를 통해 추천 문제들을 풀어보자!  
<br/>
혹시 **단계별**로 랜덤으로 풀기 원하는 사람은 아래를 이용하면 된다.  
<br/>
<a href="javascript:randomlink_bronze()">![Bronze](https://static.solved.ac/tier_small/1.svg){: width='20' height='auto'}무작위 풀어보기</a>  
<a href="javascript:randomlink_silver()">![Silver](https://static.solved.ac/tier_small/7.svg){: width='20' height='auto'}무작위 풀어보기</a>  
<a href="javascript:randomlink_gold()">![Gold](https://static.solved.ac/tier_small/13.svg){: width='20' height='auto'}무작위 풀어보기</a>  
<a href="javascript:randomlink_platinum()">![Platinum](https://static.solved.ac/tier_small/19.svg){: width='20' height='auto'}무작위 풀어보기</a>  
<a href="javascript:randomlink_diamond()">![Diamond](https://static.solved.ac/tier_small/25.svg){: width='20' height='auto'}무작위 풀어보기</a>  

# <center>그리디</center>

<div id='greedy'>
  <style>
    table { margin-bottom: 5em }
    tr, td, th { width: 1%;  font-size:1em; }
    td, th { text-align: center }
  </style>
</div>

# <center>완전 탐색</center>

<div id='bruteforce'>
  <style>
    table { margin-bottom: 5em }
    tr, td, th { width: 1%;  font-size:1em; }
    td, th { text-align: center }
  </style>
</div>

# <center>깊이 우선 탐색 (DFS)</center>

<div id='dfs'>
  <style>
    table { margin-bottom: 5em }
    tr, td, th { width: 1%;  font-size:1em; }
    td, th { text-align: center }
  </style>
</div>
