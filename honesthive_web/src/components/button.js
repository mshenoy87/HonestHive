import react from 'react';

export function ValidateButton(props) {

    const handleClick = (event) => {
        event.preventDefault();
    }

    return <div>  
                <button type={props.type} className={props.className}>Analyze</button>
            </div>
}