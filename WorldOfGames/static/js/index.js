window.onload = () => {
    let interval = setInterval(async () => {
        try {
            let json = await fetch("/score")
            let score = await json.json()
            el = document.getElementsByClassName("success")[0]
            if (el && el.textContent && el.textContent != score)
                window.location.reload()
        }
        catch (err) {
            console.log(`An error occurred: ${e}`)
        }
    }, 10000)
}