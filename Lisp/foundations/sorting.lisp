;;; Insertion sort
(defun insertion-sort (A)
  (let ((lst A)
	(key 0)
	(i 0))
    (loop for j from 1 to (- (length lst) 1)
	 do
	 (setf key (nth j lst))
	 (setf i (- j 1))
	 (while (and (>= i 0) (> (nth i lst) key))
	   (setf (nth (+ i 1) lst)
		 (nth i lst))
	   (setf i (- i 1)))
	 (setf (nth (+ i 1) lst) key))
    lst))

;;; Utilities
(defmacro while (test &body body)
  `(do ()
       ((not ,test))
     ,@body))
