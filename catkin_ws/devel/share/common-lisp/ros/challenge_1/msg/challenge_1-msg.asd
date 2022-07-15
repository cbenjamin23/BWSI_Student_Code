
(cl:in-package :asdf)

(defsystem "challenge_1-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "flip" :depends-on ("_package_flip"))
    (:file "_package_flip" :depends-on ("_package"))
    (:file "state" :depends-on ("_package_state"))
    (:file "_package_state" :depends-on ("_package"))
  ))