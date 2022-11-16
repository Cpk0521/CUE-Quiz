//dir
var img_dir = './images'
var music_dir = './music';

//data
var songlist = {}
var songtype = {}
var discolist = {}
var discotype = {}

//quiz
var quizmode = 0
var questions = [];
var correct = 0;
var curr = 0;
var refresTime = 0;
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

shuffle = (arr) => {
    arr.sort(() => Math.random() - 0.5);
}

createquiz = (arrlist) => {
    
    refresTime = 3
    $('#refresh_btn').removeClass('lock');

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

    shuffle(questions);

    //for test
    // questions = questions.slice(-5);
    
    showQuestion(questions[curr], quizmode)
}

showQuestion = (question, mode) => {

    $('#quiz_question').removeClass('d-none')
    $('#quiz_answer').addClass('d-none')

    //清除上次所選擇的選項
    $('#quiz_options>div.option_button').removeClass('is-selected');


    if(mode == 1){
        $('#refresh_btn').addClass('d-none');    
    }else{
        $('#refresh_btn').removeClass('d-none');    
    }

    //鎖上按鈕
    $('#play_btn').addClass('lock');
    $('#refresh_btn').addClass('lock');
    $('#ans_confirm > button.confirm_button').removeClass('active').addClass('not_active');
    $('#quiz_confirm > button.confirm_button').removeClass('active').addClass('not_active');

    //把答案填入選項
    for (let index = 0; index < question.answers.length; index++) {
        $('#quiz_options>div.option_button>span').eq(index).text(question.answers[index]);
    }

    player = new Howl({
        src: [`${music_dir}/${question.song}`],
        html5: true,
        onload: ()=>{
            // let offset = Math.floor(Math.random() * (player._duration - 10) + 1);

            // player._sprite.randomclip = [offset*1000, 10000];

            // player.play('randomclip');
            AudioClip(mode)

            $('#play_btn').removeClass('lock');

            if (refresTime > 0) {
                $('#refresh_btn').removeClass('lock');   
            }
        },
        onplay: ()=>{
            $('#play_btn').html(ispause(false))
        },
        onpause: ()=>{
            $('#play_btn').html(ispause(true))
        },
        onstop: ()=>{
            $('#play_btn').html(ispause(true))
        },
        onend: ()=>{
            $('#play_btn').html(ispause(true))
        }
    })
}

AudioClip = (mode) => {
    console.log(mode)
    if(player){

        if (player.playing()){
            player.stop();
        }

        if(mode == 1) {
            player._sprite.randomclip = [0, 1700];
        }else{
            let offset = Math.floor(Math.random() * (player._duration - 10));
            player._sprite.randomclip = [offset*1000, 10000];
        }

        player.play('randomclip');
    }
}

ispause = (bool) => {

    if(bool) {
        return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M7 4v16l13 -8z"></path>
                </svg>`
    }

    return `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-player-pause" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <rect x="6" y="5" width="4" height="14" rx="1"></rect>
                <rect x="14" y="5" width="4" height="14" rx="1"></rect>
            </svg>`
}

showAnswer = (choice, question) => {

    $('#quiz_question').addClass('d-none')
    $('#quiz_answer').removeClass('d-none')

    $('#ans_SongName').children('span').removeClass('correct').removeClass('wrong').html(question.correct);

    if(choice == question.correct){
        correct++;
        $('#ans_SongName').children('span').addClass('correct');
    }else{
        $('#ans_SongName').children('span').addClass('wrong');
    }

    $('#ans_disco').html('')

    questions[curr].discos.forEach(id => {
        
        let discodata = discolist.find(element => element.id == id.disco);

        let pdev = `<div class="disco_item">
                        <img class='discoimg' src="${img_dir}/CDimg/${discodata.cover[0].file}">
                        <span>${discodata.title}</span>
                        <span>${discodata.name}</span>
                    </div>`

        $('#ans_disco').append(pdev);

        if(discodata.lnkto != "")
        {
            $('.discoimg').click(function(e) {
                e.preventDefault();
                window.open(discodata.lnkto);
    
            });
        }

    });

    curr++;

    $('#ans_confirm > button.confirm_button').removeClass('not_active').addClass('active');
}

ShowResult = () => {
    
    $('#quiz_answer').addClass('d-none').removeClass('d-show')
    $('#quiz_question').addClass('d-none').removeClass('d-show')
    $('#quiz').addClass('d-none').removeClass('d-show')
    
    //result
    $('#result').removeClass('d-none').addClass('d-show').fadeIn('slow');

    let percentage = Math.floor(correct/questions.length * 100);

    $('#result_word>span>span').eq(0).text(questions.length);
    $('#result_word>span>span').eq(1).text(correct).addClass('correct');

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

    $('#rankimg').attr('src', `./images/ranking/ClassIconL_${ranking}.png`);
    
    let q = '';
    switch (quizmode) {
        case 1:
            q = 'イントロ編';
            break;
    
        default:
            q = 'ランダム全曲編';
            break;
    }

    $('#twitter').attr('href', `https://twitter.com/intent/tweet?text=キュー楽曲検定！${q}%0a全${questions.length}問中${correct}問正解！%0a&hashtags=キュー,キュー楽曲檢定&url=https://cpk0521.github.io/CUE-Quiz/%0a`)
}


//關卡選擇
$('#level_select_options>div.option_button').click(function(){
    $('div.option_button').removeClass('is-selected');
    $(this).addClass('is-selected');
    $('#level_select_confirm > button.confirm_button').removeClass('not_active').addClass('active');
})


//Quiz開始
$('#level_select_confirm > button.confirm_button').click(()=>{
    $('#level_selection').addClass('d-none');

    let mode = $('.option_button.is-selected').children('span').text()

    if(mode == '' || mode == undefined || mode == null){
        return
    }

    if(mode == 'イントロ編') {
        console.log('イントロ編');
        quizmode = 1;
        createquiz(songlist.filter(song => song.songtype == 1));
    }

    if(mode == 'ランダム全曲編') {
        createquiz(songlist);
    }

    $('#quiz').removeClass('d-none')
    $('#quiz').fadeIn('slow');
})


//問題答案選擇
$('#quiz_options>div.option_button').click(function(){
    $('div.option_button').removeClass('is-selected');
    $(this).addClass('is-selected');
    $('#quiz_confirm > button.confirm_button').removeClass('not_active').addClass('active');
})

//顯示問題答案
$('#quiz_confirm > button.confirm_button').click(function(){

    if(player) {
        player.stop();
        player.unload();
        player = null;
    }

    let choice =  $('#quiz_options>div.option_button.is-selected').children('span').text();
    
    showAnswer(choice, questions[curr])
})

//下一題
$('#ans_confirm > button.confirm_button').click(function(){

    if(curr == questions.length) {
        ShowResult()
    } else {
        showQuestion(questions[curr], quizmode)
    }

})

$('#reQuiz').click(()=>{
    location.reload();
})


$('#play_btn').click(()=>{
    if (player.playing()) {
        player.stop();
    } else {
        player.play('randomclip');
    }
})

$('#refresh_btn').click(()=>{

    if ((!$('#refresh_btn').hasClass('lock')) && (refresTime > 0)) {

        if (player.playing()) {
            player.stop();
        }

        $('#refresTime').html(--refresTime);
        if(refresTime == 0)
        {
            $('#refresh_btn').addClass('lock');
        }
    
        AudioClip(quizmode);
    }
})