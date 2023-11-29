console.log("Hello world");

document.getElementById("feature-form").addEventListener("submit",(event)=>{

    event.preventDefault();

    const formInputs = document.querySelectorAll(".form-input");

    const formValues = {};

    formInputs.forEach((input)=>{

        const name = input.name;
        const value = input.value;

        formValues[name] = value;
    });

    console.log(formValues);
});