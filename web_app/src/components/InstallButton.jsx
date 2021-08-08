import { useEffect, useState } from 'react';

let deferredPrompt;  
    
export default function InstallButton() {
  const container = {
    margin: "4rem",
  };

  const [installable, setInstallable] = useState(false);

  useEffect(() => {
    window.addEventListener("beforeinstallprompt", (e) => {
      // Prevent the mini-infobar from appearing on mobile
      e.preventDefault();
      // Stash the event so it can be triggered later.
      deferredPrompt = e;
      // Update UI notify the user they can install the PWA
      setInstallable(true);
    });

    window.addEventListener('appinstalled', () => {
      // Log install to analytics
      console.log('INSTALL: Success');
    });
  }, []);

  const handleInstallClick = (e) => {
      // Hide the app provided install promotion
      setInstallable(false);
      // Show the install prompt
      deferredPrompt.prompt();
      // Wait for the user to respond to the prompt
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the install prompt');
        } else {
          console.log('User dismissed the install prompt');
        }
      });
  };
  
  return (
    <div style={container}>
        <div>
          <h3>Install app:</h3>
          {installable
            ? <button className="install-button" onClick={handleInstallClick}>Install</button>
            : <p>Installation is not available. (Is the app already installed, or does your broweser support this feature?)</p>
          }
        </div>
    </div>
  );
};