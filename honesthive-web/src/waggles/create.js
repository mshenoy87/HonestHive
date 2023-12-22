import React from "react";
import { createWaggle } from "./lookup";

export function WaggleCreate(props) {
    const textAreaRef = React.createRef();
    const {didWaggle} = props;
  
    const handleBackendUpdate = (response, status) => {
      if (status === 201) {
        didWaggle(response);
      } else {
        console.log(response);
        alert("An error occurred, please try again: ", status);
      }
    }
  
    const handleSubmit = (event) => {
      event.preventDefault();
      // when submitted by user, update the map of waggle
      let newWaggleText = textAreaRef.current.value;
      createWaggle(newWaggleText, handleBackendUpdate);
  
      textAreaRef.current.value = "";
    }
  
    return <div className={props.className}>
              <form onSubmit={handleSubmit}>
                <textarea ref={textAreaRef} required={true} className='form-control' name='waggleText' placeholder='Your waggle'>       
                </textarea>
                <button type='submit' className='btn btn-primary'>Waggle</button>
              </form>
            
            </div>
  }
  