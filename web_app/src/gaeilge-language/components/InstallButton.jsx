// import { useEffect, useState } from 'react';

// let deferredPrompt;  
    
export default function InstallButton() {
  const container = {
    margin: "4rem",
  };

  // all of this commented out code was for the dyamic button, I may revisit this to try and fix its functionality at a later date

  // const [installable, setInstallable] = useState(false);

  // useEffect(() => {
  //   window.addEventListener("beforeinstallprompt", (e) => {
  //     // Prevent the mini-infobar from appearing on mobile
  //     e.preventDefault();
  //     // Stash the event so it can be triggered later.
  //     deferredPrompt = e;
  //     // Update UI notify the user they can install the PWA
  //     setInstallable(true);
  //   });

  //   window.addEventListener('appinstalled', () => {
  //     // Log install to analytics
  //     console.log('INSTALL: Success');
  //   });
  // }, []);

  // const handleInstallClick = (e) => {
  //     // Hide the app provided install promotion
  //     setInstallable(false);
  //     // Show the install prompt
  //     deferredPrompt.prompt();
  //     // Wait for the user to respond to the prompt
  //     deferredPrompt.userChoice.then((choiceResult) => {
  //       if (choiceResult.outcome === 'accepted') {
  //         console.log('User accepted the install prompt');
  //       } else {
  //         console.log('User dismissed the install prompt');
  //       }
  //     });
  // };
  
  return (
    <div style={container}>
        <div>
          <h3>Install app:</h3>
          <p>For ease of use, we suggest installing this app on your device for better performance and ease of accessibility.</p>
          <p>To make this possible, this app is a PWA (progressive web app). Go to your browser settings and click the option "Install Best Bus".</p>
          <p>Unfortunatley, some browsers and devices do not support this feature.</p>
          {/* The below code shows an installation button, however the feature has issues with only firing once and in certain conditions */}
          {/* Mnaual install is probably best for now */}
          {/* {installable
            ? <button className="install-button" onClick={handleInstallClick}>Install</button>
            : <p><b><i></i>Installation is not available.</b></p>
          } */}
        </div>
    </div>
  );
};