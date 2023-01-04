function check_answer(answer) {
    var answer_key = answer
    for (var i = 0; i < 20; i++) {
        element = document.getElementsByName((i).toString())
        for (var j = 0; j < 4; j++) {
            (function (index) {
                element[j].onclick = () => {
                    var ans = document.getElementsByName((index).toString())
                    var text = document.getElementById((index).toString())
                    for (let k of ans) {
                        if (k.checked) {
                            if (k.value == answer_key[index]) {
                                text.innerHTML = "correct!"
                            }
                            else {
                                text.innerHTML = ""
                            }
                        }
                    }
                }
            })(i)
        }
    }
}