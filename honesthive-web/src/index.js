import React, { StrictMode } from 'react';
import ReactDOM, { createRoot } from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { WaggleComponent, FeedComponent } from './waggles';

import App from './App';
import { ProfileBadgeComponent } from './profile';

const appEl = document.getElementById('root')
if (appEl) {
  const root = createRoot(appEl);
  root.render(<App />, appEl);
}

const el = document.getElementById("Honest-Hive");
if (el) {
  // renders the elements given the data set taken from the "Honest-Hive" div in index.js
  const WaggleElement = createRoot(el);
  WaggleElement.render(
    <StrictMode>
      <WaggleComponent {...el.dataset}/>
    </StrictMode>
  );
  
}

const domContainer = document.getElementById('Honest-Hive-Feed');
if (domContainer) {
  const feed = createRoot(domContainer);
  if (feed) {
    feed.render(<StrictMode>
      <FeedComponent {...domContainer.dataset}/>
      </StrictMode>
    )
  }
}

const userProfile = document.querySelector("#HH-profile-badge");
// userProfile.forEach(container => {
//   ReactDOM.render(
//     React.createElement(ProfileBadgeComponent, container.dataset), container)
// });
if (userProfile) {
  const root = createRoot(userProfile);
  if (root) {
    root.render(<StrictMode>
      <ProfileBadgeComponent username={userProfile.dataset.username} />
      </StrictMode>)
  }
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
// ServiceWorker.unregister()