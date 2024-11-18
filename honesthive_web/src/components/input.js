import React, {useState} from "react";
import { ValidateButton } from "./button";
import './../styles/style.css';



export function UserInput(props) {
    const {setStatement} = props;
    const textAreaRef = React.createRef();

    // handle submit - if user clicks validate button
    const handleSubmit = (event) => {
        event.preventDefault();

        // take the user input and output into console
        let inputStatement = textAreaRef.current.value;
        console.log(inputStatement);   // test only - delete later
        setStatement(inputStatement);

        // intent: will use the data collected and send to API
        

        textAreaRef.current.value = "";

    }

    return <div className="user_input_area">
                <form onSubmit={handleSubmit}>
                    <textarea ref={textAreaRef} required className="user_input" placeholder="enter a statement" />
                    <ValidateButton type="submit" className="btn-warning"/>
                </form>
            </div>
}