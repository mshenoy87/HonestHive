import react from 'react';
import './../styles/style.css';

export function AnalysisArea(props, UserInput) {

    const {className, statement} = props;

    return <div className={className} >  

               <article>
                    <h3>Analysis Result:</h3>
                    <p><strong>Statement:</strong>{statement || "No statement has been put in"}</p>
                    <p><strong>Speaker:</strong> Donald Trump</p>
                    <p><strong>Party Affiliation:</strong> Republican</p>
                    <p><strong>Verdict:</strong> False</p>
                </article>
            </div>
}