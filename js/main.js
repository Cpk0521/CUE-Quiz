//dir
var img_dir = './image';
var music_dir = './music';

//data
var songlist;
var songtype;
var discolist;
var discotype;

//quiz
var quiztype = 0;
var questions = [];
var correct = 0;
var curr = 0;
var renewTime = 0;
var player;

//load data
$.getJSON("json/songList.json", function(data) {
    songlist = data['Songs'];
    songtype = data['SongTypes'];
})

$.getJSON("json/discography.json", function(data) {
    discolist = data['discolist'];
    discotype = data['discoTypes'];
})

function shuffle(arr) {
    arr.sort(() => Math.random() - 0.5);
}

//create quiz questions
function createquiz(arrlist){

    renewTime = 3;
    $('#renewbtn').removeClass('lock');

    arrlist.forEach(element => {
        let question = {};

        question.song = element.file;
        question.correct = element.name;
        question.discos = element.discos;

        question.answers = [];
        question.answers.push(element.name);
        while (question.answers.length < 4) {
            let randomsong = arrlist[Math.floor(Math.random() * arrlist.length)].name;
            if ($.inArray(randomsong, question.answers) == -1) {
                question.answers.push(randomsong);
            }
        }
        shuffle(question.answers);

        questions.push(question);
    });

    // questions = questions.slice(-2);

    shuffle(questions);

    switch (quiztype) {
        case 1:
            loadIntroquestion(questions[curr]);
            break;
    
        default:
            loadquestion(questions[curr]);       
            break;
    }
}


function loadquestion(question){

    $('#renewTimes').html(renewTime);

    $('#controller').addClass('d-flex').removeClass('d-none');
    $('#disco').addClass('d-none').removeClass('d-flex');

    $('#anwers').removeClass('d-none').addClass('d-flex');
    $('#checkanw').addClass('d-none').removeClass('d-block');

    $('#soundbtn').addClass('lock');
    $('#renewbtn').addClass('lock');

    for (let index = 0; index < question.answers.length; index++) {
        $('#anwers>div>.choosebtn>span').eq(index).text(question.answers[index]);
    }

    player = new Howl({
        src: [`${music_dir}/${question.song}`],
        html5: true,
        onload: ()=>{
            let offset = Math.floor(Math.random() * (player._duration - 10) + 1);

            player._sprite.randomclip = [offset*1000, 10000];

            player.play('randomclip');
            $('#soundbtn').removeClass('lock');

            if (renewTime > 0) {
                $('#renewbtn').removeClass('lock');   
            }
        },
        onplay: ()=>{
            $('#soundbtn>i').removeClass('fa-play').addClass('fa-pause');
        },
        onpause: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        },
        onstop: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        },
        onend: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        }
    })
}

function loadIntroquestion(question){

    $('#renewTimes').html(renewTime);

    $('#controller').addClass('d-flex').removeClass('d-none');
    $('#disco').addClass('d-none').removeClass('d-flex');

    $('#anwers').removeClass('d-none').addClass('d-flex');
    $('#checkanw').addClass('d-none').removeClass('d-block');

    $('#soundbtn').addClass('lock');
    $('#renewbtn').addClass('d-none');

    for (let index = 0; index < question.answers.length; index++) {
        $('#anwers>div>.choosebtn>span').eq(index).text(question.answers[index]);
    }

    player = new Howl({
        src: [`${music_dir}/${question.song}`],
        html5: true,
        onload: ()=>{

            player._sprite.randomclip = [0, 1700];

            player.play('randomclip');
            $('#soundbtn').removeClass('lock');
        },
        onplay: ()=>{
            $('#soundbtn>i').removeClass('fa-play').addClass('fa-pause');
        },
        onpause: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        },
        onstop: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        },
        onend: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        }
    })
}

function randClip(){
    if(player){

        if (player.playing()){
            player.stop();
        }

        let offset = Math.floor(Math.random() * (player._duration - 10));

        player._sprite.randomclip = [offset*1000, 10000];
        player.play('randomclip');
    }
}


function showanswer(discoids){

    $('#disco').html('');
    $('.confirm-btn').removeClass('selecting');

    discoids.forEach(id => {
        
        let discodata = discolist.find(element => element.id == id.disco);

        let p =`<div class='m-2'>
                    <img class='discoimg' style='cursor: pointer;' src="${img_dir}/CDimg/${discodata.cover[0].file}">
                    <p class="fontstyle-4 m-1" style="font-size: xx-small;">${discodata.title}</p>
                    <p class="fontstyle-4 m-1 fw-bold">${discodata.name}</p>
                </div>`;

        $('#disco').append(p);

        if(discodata.lnkto != "")
        {
            $('.discoimg').click(function(e) {
                e.preventDefault();
                window.open(discodata.lnkto);
    
            });
        }

    });

    $('#controller').addClass('d-none').removeClass('d-flex');
    $('#disco').addClass('d-flex').removeClass('d-none');    

    $('#anwers').removeClass('d-flex').addClass('d-none');
    $('#checkanw').addClass('d-block').removeClass('d-none'); 
}

function ShowResult(){

    $('#levelsection').addClass('d-none');
    $('#quizdiv').addClass('d-none');

    $('#result').fadeIn('slow');

    let percentage = Math.floor(correct/questions.length * 100);
    
    $('#result>div>div>p>span').eq(0).text(questions.length);
    $('#result>div>div>p>span').eq(1).text(correct).addClass('text-Danger');

    let ranking;

    if (percentage == 0) {
        //F
        ranking = 'F';
    }else if(percentage > 0 && percentage < 25){
        //E
        ranking = 'E';
    }else if(percentage >= 25 && percentage < 50){
        //D
        ranking = 'D';
    }else if(percentage >= 50 && percentage< 75){
        //C
        ranking = 'C';
    }else if(percentage >=75 && percentage < 90){
        //B
        ranking = 'B';
    }else if(percentage >= 90 && percentage < 100){
        //A
        ranking = 'A';
    }else if(percentage == 100){
        //S
        ranking = 'S';
    }

    $('#rankimg').attr('src', `./image/ranking/ClassIconL_${ranking}.png`);
    let q = '';
    switch (quiztype) {
        case 1:
            q = '???????????????';
            break;
    
        default:
            q = '?????????????????????';
            break;
    }
    $('a.twitter.confirm-btn').attr('href', `https://twitter.com/intent/tweet?text=????????????????????????${q}%0a???${questions.length}??????${correct}????????????%0a&hashtags=?????????,?????????????????????&url=https://cpk0521.github.io/CUE-Quiz/%0a`)

}

//

$('#anwers>div>div.choosebtn').click(function(){
    $('div.choosebtn').removeClass('is-selected');
    $(this).addClass('is-selected');
    $('.confirm-btn').removeClass('choosing').addClass('selecting');
})

$('#quizs>div>div.choosebtn').click(function(){
    $('div.choosebtn').removeClass('is-selected');
    $(this).addClass('is-selected');
    $('.start-btn').removeClass('choosing').addClass('selecting');
})

$('.start-btn').click(()=>{
    $('#levelsection').addClass('d-none');
    switch ($('.choosebtn.is-selected').children('span').text()) {
        case '???????????????':
            console.log('???????????????');
            quiztype = 1;
            createquiz(songlist.filter(song => song.songtype == 1));
            break;
        // case '?????????':
        //     createquiz();
        //     break;
        // case '?????????':
        //     createquiz();
        //     break;
        
        case '?????????????????????':
            createquiz(songlist);
            break;
        default:
            console.log('error');
            break;
    }
    $('#quizdiv').fadeIn('slow');
});


$('.confirm>.confirm-btn').click(function(){
    
    if ($(this).hasClass('check')) {

        $(this).removeClass('check').addClass('choosing');
        $(this).children('span').html('??????');
        
        curr++;

        if(curr < questions.length){
            switch (quiztype) {
                case 1:
                    loadIntroquestion(questions[curr]);
                    break;
            
                default:
                    loadquestion(questions[curr]);       
                    break;
            }
        }else{
            ShowResult();
        }
        
    } else {

        player.stop();
        player.unload();
        player = null;

        let ans = $('.choosebtn.is-selected').children('span').text();
        $('div.choosebtn').removeClass('is-selected');

        $(this).removeClass('selecting').addClass('check');
        $(this).children('span').html('??????');

        $('#checkanw').children('span').removeClass('text-Success').removeClass('text-Danger').html(questions[curr].correct);

        if(ans == questions[curr].correct){
            correct++;
            $('#checkanw').children('span').addClass('text-Success');
        }else{
            $('#checkanw').children('span').addClass('text-Danger');
        }

        showanswer(questions[curr].discos);
    }

});


$('.continue.confirm-btn').click(()=>{
    location.reload();
})

$('#soundbtn').click(()=>{
    if (player.playing()) {
        player.stop();
    } else {
        player.play('randomclip');
    }
})

$('#renewbtn').click(()=>{

    if ((!$('#soundbtn').hasClass('lock')) && (renewTime > 0)) {

        if (player.playing()) {
            player.stop();
        }

        $('#renewTimes').html(--renewTime);
        if(renewTime == 0)
        {
            $('#renewbtn').addClass('lock');
        }
    
        randClip();
    }
    
})