import react from 'react';

export function ValidateButton(props) {
    return <div>  
                <button type={props.type} className="btn btn-warning">Validate</button>
            </div>
}