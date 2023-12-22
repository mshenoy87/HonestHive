import React, {useState} from "react";
import { ActionButton } from "./buttons";
import { UserDisplay, UserPicture } from "../profile";

export function ParentWaggle(props) {
    const {waggle} = props;
    return waggle.parent ? <div className='col-11 mx-2 p-2'>
        <Waggle hideActions classname={''} waggle={waggle.parent} isRewaggle rewaggler={props.rewaggler}/>
        </div> : null;
}

export function Waggle(props) { 
    const {waggle, didRewaggle, hideActions, isRewaggle, rewaggler} = props;
    let className = props.className ? props.className : 'mb-auto border px-2 py-3';
    className = isRewaggle ? `${className} p-2 border rounded` : className;
    const [actionWaggle, setActionWaggle] = useState(props.waggle ? props.waggle : null)
    const path = window.location.pathname
    const match = path.match(/(?<waggleID>\d+)/)
    const urlWaggleID = match ? match.groups.waggleID : -1
    const isDetail = `${waggle.id}` === `${urlWaggleID}`;

    const handleActionPerformed = (newActionWaggle, status) => {
        if (status === 200) {
            setActionWaggle(newActionWaggle);
        } else if (status === 201) {
            if (didRewaggle) {
                didRewaggle(newActionWaggle);
            }
        }
    }
    // format waggles so that there is the message and a button for liking that message
    // For rendering the like button, the argument is what you want to pass 
        // and the parameter is not the parameter in the Like() declaration
        // so it will be the likes in the {likes} const is going to be the name in <Like/>
        // isRewaggle will mention the original user and if it is a rewaggle
    return <div className={className}>
            {isRewaggle && <span className = 'mb-2 text-muted small'>Rewaggle via @{rewaggler.username}</span>}
            <div className="d-flex">
                <div className='col-1 mx-1 py-3'>
                    <UserPicture user={waggle.user}/>
                </div>
                <div className="col-11">
                    <UserDisplay fullName user={waggle.user}/>
                    {!waggle.parent && <p>{waggle.waggleText}</p>}
                </div>
            </div>

            <div className="col-12">
                <ParentWaggle waggle={waggle} rewaggler={waggle.user}/>
            </div>

            {hideActions !== true &&
                <div className='btn px-0'>
                    <ActionButton waggle={waggle} didPerformAction={handleActionPerformed} action={{type: "like"}} className='btn btn-dark btn-md' />
                    <ActionButton waggle={waggle} didPerformAction={handleActionPerformed} action={{type: "rewaggle"}} className='btn btn-warning btn-md'/>
                </div>
            }
        </div>

}