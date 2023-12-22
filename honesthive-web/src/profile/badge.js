import React, {useState, useEffect} from 'react';
import { UserDisplay, UserPicture } from './components';
import { apiProfileDetail, apiProfileFollowToggle } from './lookup';
import {FormatCount} from './utils';


export function ProfileBadge(props) {
    const {user, didFollowToggle, profileLoading} = props;
    let followingStatus = (user && user.is_following) ? "Unfollow" : "Follow";
    // changes the verbs from follow to unfollow and back if necessary
    const handleFollowToggle = (event) => {
        event.preventDefault();
        if (didFollowToggle && !profileLoading) {
            didFollowToggle(followingStatus);
        }
    }
    // renders the profile badge on the top displaying information on the user
    return user ? <div className="m-2 ">

        <UserPicture user={user} hideLink className/>
        <div className='mt-3'><UserDisplay user={user} /></div>
        <div><FormatCount>{user.follower_count}</FormatCount> {user.follower_count === 1 ? "Follower" : "Followers"} </div>
        <div><FormatCount>{user.following_count}</FormatCount> Following</div>
        <div>{user.bio}</div>
        <button className='btn btn-primary' onClick={handleFollowToggle}>{followingStatus}</button>
    </div> : <p>Hello</p>;
}

export function ProfileBadgeComponent(props) {
    const {username} = props;
    // lookups
    const [didLookup, setDidLookup] = useState(false);
    const [profile, setProfile] = useState(null);
    const [profileLoading, setProfileLoading] = useState(false);

    // call back that finds the specific profile 
    const handleBackendLookup = (response, status) => {
        if (status===200) {
            setProfile(response);
        }
    }

    useEffect(()=> { 
        if (didLookup === false) {
            apiProfileDetail(username, handleBackendLookup);
            setDidLookup(true);
        }
    }, [username, didLookup, setDidLookup]);

    const handleNewFollow = (actionVerb) => {
        apiProfileFollowToggle(username, actionVerb, (response, status) => {
            if (status === 200) {
                // backend changes 
                setProfile(response);
            }
            setProfileLoading(false);
        })
        setProfileLoading(true)
    }

    return didLookup === false ? "Loading..." : profile ? <ProfileBadge user={profile} didFollowToggle={handleNewFollow} profileLoading={profileLoading}/> : <p>hello</p>;
}