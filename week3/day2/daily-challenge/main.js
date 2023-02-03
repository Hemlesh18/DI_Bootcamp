const button = getButton()
const shuffleButton = document.getElementById("shuffle")
button.addEventListener("click", handleclick)
shuffleButton.addEventListener("click", shuffleStories)

function getFormValues() {
    const noun = document.getElementById("noun").value
    const adjective = document.getElementById("adjective").value
    const person = document.getElementById("person").value
    const verb = document.getElementById("verb").value
    const place = document.getElementById("place").value
    return {
        noun: noun,
        adjective: adjective,
        person: person,
        verb: verb,
        place: place,
    }
}

function handleclick(e) {
    e.preventDefault()
    const getFormValues = getFormValues()
    const noun = FormValues.noun
    const adjective = FormValues.adjective
    const person = FormValues.person
    const verb = FormValues.verb
    const place = FormValues.place

    if (noun == "" || adjective == "" || person == "" || verb == "" || place == "")
        return
    console.log("all field are filled in, cool!")

    const story = writestory(noun, adjective, person, verb, place)
    console.log("story:", story)
    appendStoryToPage(story)
}

function shuffleStories() {
    const getFormValues = getFormValues()
    const noun = FormValues.noun
    const adjective = FormValues.adjective
    const person = FormValues.person
    const verb = FormValues.verb
    const place = FormValues.place
}

function appendStoryToPage(story) {
    const paragraph = document.getElementById("story")
    const span = document.createElement("span")
    span.innerText = story
    paragraph.appendChild(span)

}

function writestory(noun, adjective, person, verb, place) {
    return "i like to look at ${noun}s, i think that they are ${adjective}. my favorite person is ${person}. we often ${verb}together whem we are in ${place} "
}

function getButton() {
    return document.getElementByID("lib-button")
}