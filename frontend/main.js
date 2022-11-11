// information to reach API
const urlCreateQuery = 'http://127.0.0.1:8000/createquery/';
const urlConfirmGT = 'http://127.0.0.1:8000/updatequery/'

// Some page elements
const searchButton = document.getElementById('searchquery');
const inputField = document.getElementById('inputquery');
const respondField = document.getElementById('responseField');
// const selectionLabel = document.querySelectorAll('label');
const sentenceBERTLabel = document.querySelectorAll('label[for^="SentenceBERT"]');
const BERTScoreLabel = document.querySelectorAll('label[for^="BERTScore"]');
const sentenceBERTSelectionInput = document.querySelectorAll('input[name="SentenceBERTprediction"]');
const BERTScoreSelectionInput = document.querySelectorAll('input[name="BERTScorePrediction"]');
const submitButton = document.getElementById('confirmGT');

const MODELS = ['sentenceBERT',"BERTScore"];
const inputLabel = {"sentenceBERT":sentenceBERTLabel,
                    "BERTScore":BERTScoreLabel}
const selectionInput = {'sentenceBERT':sentenceBERTSelectionInput,
                        'BERTScore':BERTScoreSelectionInput}
var idList = {};

// Asynchronous functions
async function createQuery(event){
    event.preventDefault();
    const thisquery = inputField.value;
    const jsonquery = JSON.stringify({query: thisquery});
    // const jsonquery ={'query':thisquery};
    try {
        const response = await fetch(urlCreateQuery,{
            method:"POST",
            body:jsonquery,
            headers:{'Content-Type': 'application/json','accept':'application/json'},
        })
        if (response.ok){
            const jsonResponse = await response.json();
            for (let index = 0; index < MODELS.length; index++) {
                const modelName = MODELS[index];
                const thisJson = jsonResponse[modelName]
                let predictions = [];
                for(let key in thisJson){
                    predictions.push(thisJson[key]);
                }
                for(let i = 0; i < inputLabel[modelName].length-1; i++){
                    inputLabel[modelName][i].innerHTML=predictions[i+1];
                }
                // counter.innerHTML = `${predictions[0]}`;
                idList[modelName]=parseInt(predictions[0]);
            }
            respondField.style.display = 'block';
            inputField.readOnly = true;
            searchButton.disabled = true;
        }
        else{
            throw new Error('The response is invalid!');
        }
    } catch (error) {
        alert(`Something is wrong: ${error}`);
    }
}

async function confirmGroundTruth(event){
    event.preventDefault();
    var body = [];
    for (let index = 0; index < MODELS.length; index++) {
        const modelName = MODELS[index];
        var gt = -2;
        for (let index = 0; index < selectionInput[modelName].length; index++) {
            var thisGT = selectionInput[modelName][index];
            if (thisGT.checked){
                gt = index;
                break;
            }
        }
        let this_id = idList[modelName];
        let this_json = {id:this_id,selection:gt};
        // this_json = JSON.stringify({this_json})
        body.push(this_json)
    }
    const jsonquery = JSON.stringify(body);
    // const jsonquery = body
    try {
        const response = await fetch(urlConfirmGT,{
            method:"PUT",
            body:jsonquery,
            headers:{'accept':'application/json','Content-Type': 'application/json'},
        })
        if (response.ok) {
            var isSaved = true;
            const jsonResponse = await response.json();
            for (let index = 0; index < MODELS.length; index++) {
                const modelName = MODELS[index];
                let id = idList[modelName];
                if (jsonResponse[id].status != 1) {
                    alert(`Something is wrong, your confirmation is not saved! Error info: ${id}}`);
                    isSaved = false;
                }
            }
            if(isSaved){
                alert("Congrats! Your confirmation has been received!");
                location.reload();
            }
        }
    } catch (error) {
        alert(`Something is wrong: ${error}`);
    }
}

function test(event){
    event.preventDefault();
    // searchButton.style.color = 'green';
    alert(selectionList[0].checked);
}

searchButton.addEventListener('click',createQuery);
submitButton.addEventListener('click',confirmGroundTruth);