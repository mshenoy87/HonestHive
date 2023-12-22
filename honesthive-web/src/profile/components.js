import React from "react";

export function UserLink (props) {
    const {username} = props;
    const handleUserLink = (event) => {
        window.location.href = `/profiles/${username}/`;
    }
    return <span className="pointer" onClick={handleUserLink}>
        {props.children}
    </span>
}

export function UserPicture (props) {
    const {user, hideLink} = props;
    const UserID = <span className="mx-1 px-3 py-3 rounded-circle bg-dark text-white">{user.username[0]}</span>
    return hideLink === true ? UserID : <UserLink username={user.username}>{UserID}</UserLink>
}

export function UserDisplay (props) {
    const {user, fullName} = props;
    const nameDisplay = fullName ? `${user.first_name} ${user.last_name}` : null;

    return <React.Fragment>
        <UserLink username={user.username}>@{user.username} </UserLink>
        <div><span className="text-muted small">{nameDisplay}</span></div>
    </React.Fragment> 
}
